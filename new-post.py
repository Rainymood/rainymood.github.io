
import argparse


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="Name of new post with dashes")
    # parser.add_argument("name", type=str, help="Name of new post")
    # args = parser.parse_args()
    title = input("Input name of title: ")
    import datetime
    import os
    date = datetime.date.today().strftime("%Y-%m-%d")
    slug = date + "-" + title.replace(" ", "-").lower()
    filename = slug + ".md"
    print(f"Write file _posts/{filename}")
    print(f"Create dir assets/{slug}")
    with open(os.path.join("_posts", filename), "w") as f:
        pass
    os.makedirs(os.path.join("assets", slug))
    # print("Assert we are on master branch")
    # print("Creating new post")
    # print("Input name of the post: ...")
    # print("Git checkout -b YYMMDD-name-of-post")
    # print("Creating new post with base post YYYY-MM-DD-name-of-post.md")
    # print("Adding thumbnail")
    # print("Creating asset directory YYYY-MM-DD-name-of-post/")