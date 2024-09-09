""""Prompts the user to input a title ("new title") this then gets slugified and
the asset folder (assets/YYYY-MM-DD-new-title) gets made and the markdown file
gets made (_posts/YYYY-MM-DD-new-title)."""
import datetime
import os
import unicodedata
import re
import shutil

def header(title: str, date, asset_dirname: str) -> str:
    """Returns the header to be written to the md file"""

    # TODO: fix https://stackoverflow.com/questions/2504411/proper-indentation-for-multiline-strings
    assert len(title) > 0
    assert len(asset_dirname) > 0

    return f"""---
title: "{title}"
date: {date.strftime("%Y-%m-%d")}
tags:
# Blog or how-to
- blog
- tutorial

# Work or personal?
- work
- personal

# Start here themes
- systems
- software
- learning
- product
- career

# Big themes that I write about
- engineering
- software architecture
- management
- leadership
- productivity
- lean
- memory palace

# gaming/ui/ux design
- juice
- game design

# Programming languages/Cloud
- rust
- golang
- python
- sql
- javascript
- aws
- testing
- documentation

# Smaller themes
- writing
- product
- design
- tools
- advent of code
- aws 
- docker
- machine learning
- programming
- pytorch
- tensorflow
- code
- show-your-work
- tip
- athena

- meta programming

- flashcards
- projects
- startups

- cosmicpython
- inversion of control
- domain driven design

- story
- lessons learned
- video games

categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/{asset_dirname}/thumbnail.png"
---
<!-- ctrl + alt + v -->

<!-- Checklist:
Title = insight
Interesting 1st sentence
Short and concise -->

<!-- Do the most annoying thing first: thumbnail creation -->

https://app.bannerbear.com/projects/POobgvMNDkxzxAYW70/templates/3g8zka5Y2OlaDEJXBY

https://www.photopea.com/

<!-- 1. interesting hook -->

YOU ARE NOT FAMOUS. So do whatever you want :)

SP001: Establish yourself as an expert in the following fields: systems, learning, career, product, software.

* What do I want to say
* Why do I want to say it?
* How does this make a better product?
* How does this make a better org?

"""

def footer():
    """Should probably use textwrap.dedent here..."""
    return """
# Subscribe

<!-- Begin Mailchimp Signup Form -->
<link href="//cdn-images.mailchimp.com/embedcode/horizontal-slim-10_7.css" rel="stylesheet" type="text/css">
<style type="text/css">
#mc_embed_signup{background:#fff; clear:left; font:14px Helvetica,Arial,sans-serif; width:100%;}
/* Add your own Mailchimp form style overrides in your site stylesheet or in this style block.
    We recommend moving this block and the preceding CSS link to the HEAD of your HTML file. */
</style>
<div id="mc_embed_signup">
<form action="https://gmail.us3.list-manage.com/subscribe/post?u=92fe86c389878585bc87837e8&amp;id=50543deff9" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="validate" target="_blank" novalidate>
    <div id="mc_embed_signup_scroll">
<label for="mce-EMAIL">I blog about how to grow as a machine learning engineer! Liked this article and want to hear more? Join 40+ others and subscribe!</label>
<input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>
    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_92fe86c389878585bc87837e8_50543deff9" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>
<!--End mc_embed_signup-->
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

ASSET_DIR = "assets"

if __name__ == "__main__":
    # Request input from user
    title = input("Title of blog post (Ctrl + C to cancel): ")
    slug = slugify(title)
    print("Creating a new blog post for you...")
    print("\tTitle: ", title)
    print("\tSlug: ", slug)

    today = datetime.date.today()
    asset_dirname = today.strftime("%Y-%m-%d") + "-" + slug # ex 2022-05-20-title-of-new-post
    markdown_filename = asset_dirname + ".md" # 2022-05-20-title-of-new-post.md
    print("\tAsset dir: ", asset_dirname)
    print("\tFilename: ", markdown_filename)

    # "Tests"
    assert len(asset_dirname) > 0, "Foldername can't be empty"
    assert len(title) > 3, "Title should be longer than 3 chars"
    assert " " not in markdown_filename, "No spaces allowed in filename"
    assert markdown_filename.endswith(".md"), "Filename should end with .md extension"
    assert markdown_filename.startswith("202"), "Filename should start with YYYY-MM-DD"

    # Create asset dir
    asset_dirpath = os.path.join(ASSET_DIR, asset_dirname)
    os.makedirs(asset_dirpath, exist_ok=True)
    print(f"\tSuccessfully created {asset_dirpath}")

    # Create thumbnail
    default_thumbnail_path = os.path.join(ASSET_DIR, "images","default-thumbnail.png")
    post_thumbnail_path = os.path.join(ASSET_DIR, asset_dirname, "thumbnail.png")
    print(f"\tCopying {default_thumbnail_path} -> {post_thumbnail_path}")
    shutil.copy(default_thumbnail_path, post_thumbnail_path)

    # Create markdown file
    markdown_filepath = os.path.join("_posts", markdown_filename)
    with open(markdown_filepath, "w") as f:
        md_header = header(title, today, asset_dirname)
        md_footer = footer()
        f.write(md_header)
        f.write(md_footer)
    print(f"\tSuccessfully created {markdown_filepath}")

    print(f"\tHave fun writing!")