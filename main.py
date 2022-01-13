#!/bin/env python3

# Copyright 2015  Malcolm Inglis <http://minglis.id.au/>


import os
import sys
from datetime import datetime
from argparse import ArgumentParser, ArgumentTypeError
from subprocess import check_output, CalledProcessError, Popen, PIPE, DEVNULL
from contextlib import contextmanager


class FileExistsException(Exception):
    def __init__(self, path):
        self.path = path


def main():
    args = parse_args(sys.argv[1:])
    try:
        path = jekyll_post(args)
    except FileExistsException as ex:
        print('A file already exists at \'{}\'.'.format(ex.path),
              file=sys.stderr)
        return 1
    if path != '-':
        print(path)
    return 0


def parse_args(raw_args):
    args = make_parser().parse_args(raw_args)
    args.date = args.date or now()
    args.attributes = args.attributes or []
    return args



def make_parser():
    p = ArgumentParser(description='Creates a new Jekyll post, and prints its '
                                   'path to standard out.')

    p.add_argument('title', type=escape_str,
                   help='The title for the new post.')

    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument('-c', '--category',
                   help='The path of the category directory for the new post, '
                        'such that it will be written into '
                        '\'$JEKYLL_SITE_PATH/$category/_posts\'. ')
    g.add_argument('-d', '--directory', type=directory_exists,
                   help='The path of the directory to write the new post '
                        'into.')
    g.add_argument('-o', '--output', metavar='PATH',
                   help='The path to write the new post to. Provide \'-\' to '
                        'write to standard out.')
    p.add_argument('-t', '--date', type=parse_datetime,
                   help='The date and time for the new post, in a format '
                        'accepted by the `date` utility. Default: now.')
    p.add_argument('-x', '--extension', default='md',
                   help='The file extension for the new post. '
                        'Default: \'md\'.')
    p.add_argument('-a', '--attributes', nargs="*", metavar='ATTR',
                   help='Extra attributes to put in the header, provided in a '
                        'format according to \'jekyll-post-header\'. The '
                        '\'layout\' attribute defaults to \'default\'.')
    p.add_argument('-p', '--padding', type=int, default=10, metavar='NSPACES',
                   help='The number of spaces to left-align the attributes '
                        'by. Default: 10.')

    return p


def escape_str(s):
    return s.replace('\'', '\\\'')


def directory_exists(s):
    if not os.path.isdir(s):
        raise ArgumentTypeError('\'{}\' is not a directory.'.format(s))
    return s


def parse_datetime(s):
    try:
        ds = check_output(['date', '--date={}'.format(s),
                           '--iso-8601=seconds'],
                          stderr=DEVNULL).decode().strip()
    except CalledProcessError:
        raise ArgumentTypeError(('\'{}\' is an invalid date. It must be in a '
                                 'format accepted by the `date` utility\'s '
                                 '`--date` argument.').format(s))
    return datetime.strptime(ds, '%Y-%m-%dT%H:%M:%S%z')


def now():
    return parse_datetime(datetime.now().isoformat())


def jekyll_post(args):
    with header_proc(args) as proc:
        path = get_post_path(args)
        with open_post_file(path) as file:
            for bline in proc.stdout:
                line = bline.decode()[:-1]
                print(line, file=file)
        return path


def get_post_path(args):
    if args.output:
        return args.output
    else:
        filename = check_output(['jekyll-post-filename', args.title,
                                 '--date', args.date.strftime('%Y-%m-%d'),
                                 '--extension', args.extension],
                                stderr=DEVNULL).decode()[:-1]
        dirname = (args.directory
                   or os.path.join(os.environ.get('JEKYLL_SITE_PATH', ''),
                                   args.category,
                                   '_posts'))
        return os.path.join(dirname, filename)


@contextmanager
def open_post_file(path):
    if path == '-':
        yield sys.stdout
    else:
        if os.path.exists(path):
            raise FileExistsException(path)
        with open(path, 'w') as f:
            yield f


def header_proc(args):
    # TODO: this won't raise an exception if the script fails. Is there a way to
    # check for errors, while still streaming the output?
    return Popen(['jekyll-post-header', '--padding', str(args.padding),
                  'layout:"default"',
                  'date:"{}"'.format(args.date),
                  'title:"{}"'.format(args.title)]
                 + args.attributes,
                 stdout=PIPE, stderr=DEVNULL)


if __name__ == '__main__':
    rv = main()
    sys.exit(rv)
