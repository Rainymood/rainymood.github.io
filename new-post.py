
""""Prompts the user to input a title ("new title") this then gets slugified and
the asset folder (assets/YYYY-MM-DD-new-title) gets made and the markdown file
gets made (_posts/YYYY-MM-DD-new-title)."""
import datetime
import os
import unicodedata
import re

def header(title: str, date, asset_dirname: str) -> str:
    """Returns the header to be written to the md file"""

    # TODO: fix https://stackoverflow.com/questions/2504411/proper-indentation-for-multiline-strings
    assert len(title) > 0
    assert len(asset_dirname) > 0

    return f"""---
title: "{title}"
date: {date.strftime("%Y-%m-%d")}
tags:
- blog
- jekyll
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/{asset_dirname}/thumbnail.png"
---

# Hello world
"""

def slugify(value, allow_unicode=False) -> str: 
    """
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')

if __name__ == "__main__":
    title = input("Input name of title (ctrl + C to cancel): ")
    print(title)
    print("slugify titled", slugify(title))

    today = datetime.date.today()
    asset_dirname = today.strftime("%Y-%m-%d") + "-" + slugify(title) # ex 2022-05-20-title-of-new-post
    markdown_filename = asset_dirname + ".md" # 2022-05-20-title-of-new-post.md
    print("foldername: ", asset_dirname)
    print("filename: ", markdown_filename)

    # "Tests"
    assert len(asset_dirname) > 0, "Foldername can't be empty"
    assert len(title) > 3, "Title should be longer than 3 chars"
    assert " " not in markdown_filename, "No spaces allowed in filename"
    assert markdown_filename.endswith(".md"), "Filename should end with .md extension"
    assert markdown_filename.startswith("2022"), "Filename should start with YYYY-MM-DD" # todo

    # Create asset dir
    asset_dirpath = os.path.join("assets", asset_dirname)
    os.makedirs(asset_dirpath, exist_ok=True)
    print(f"Successfully created {asset_dirpath}")

    # Create markdown file
    markdown_filepath = os.path.join("_posts", markdown_filename)
    with open(markdown_filepath, "w") as f:
        md_header = header(title, today, asset_dirname)
        f.write(md_header)
    print(f"Successfully created {markdown_filepath}")