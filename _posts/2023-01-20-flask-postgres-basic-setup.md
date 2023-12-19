---
title: "Flask Postgres basic setup"
date: 2023-01-20
tags:
- python
- flask
- postgres
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2023-01-20-flask-postgres-basic-setup/thumbnail.gif"
---
<!-- ctrl + alt + v -->

In this blog post I'll share a basic [Flask](https://flask.palletsprojects.com/en/2.2.x/) and [PostgreSQL](https://www.postgresql.org/) setup that you can use for local development.

![](/../assets/2023-01-20-flask-postgres-basic-setup/image.gif)

This tiny prototype:
* Creates a postgres database
* Inserts some data in this database
* Runs a flask api
* Exposes an endpoint to add data to the database
* Fetches the results from the database and renders them

I learned:
* How to create a postgres database
* How to create tables in a postgres database
* How to grant postgres users privileges
* How to connect to a postgres database with python
* How to insert data in a postgres with python
* How to fetch data from a postgres with python
* How to make flask and postgres talk to each other

Full code can be found [here](https://github.com/Rainymood/flask-postgres).

Credits go to this [tutorial](https://www.digitalocean.com/community/tutorials/how-to-use-a-postgresql-database-in-a-flask-application).

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
    