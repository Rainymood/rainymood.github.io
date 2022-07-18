---
title: "Show your work: Writing complex SQL queries"
date: 2022-05-10
tags:
  - sql
  - aws
  - athena
  - show-your-work
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2022-05-10-show-your-work-sql/thumbnail.png"
---

This week I had to write this monster of an SQL query and I wanted to share some
tips that I found useful.

<!-- Behold, the SQL monster under your bed:

![](/../assets/2022-05-10-show-your-work-sql/2022-05-10-16-34-17.png) -->

# Tip 1: Start with a docstring

My first tip is to start complex SQL queries with a docstring explaining the
what and the why of the query.

SQL is code and it should be treated as such. Especially for larger queries like
these that can be complex to understand if you see them for the first time,
start with a docstring! 

```sql
/* Create-repopulation-for-default-difficulties.sql

Creates the table that is needed for continuous calibration (CC). We create this
table because we want to revert all previously continuously calibrated
difficulties from ... to ...

Revert all events that:
    1. Had no event before that date, but had an event after
    2. Had a default difficulty event before that date and an event after
*/
```

# Tip 2: Use CTEs liberally

The second tip is to use Common Table Expressions (CTEs) liberally. 

Complex things are just many simple things on top of another. This also holds
true in SQL queries, a complex SQL query can often be broken down into multiple
easier queries. 

CTEs are great for this because CTEs (or as I like to call them "subtables") are temporary tables that you can use to get to your final query output. 

In this big query I use three CTEs that all work towards the final output.  The
first CTE grabs all the calibrated exercises that we need to look at 

```sql
with calibrated_exercises as (
    ...
), 
```

The second CTE considers all the events in our calibration warehouse prior to a certain date

```sql
previous_events as (
    ...
), 
```

Then the final CTE has all the events after

```sql
after_events as (
    ...
)
```

And then we use these CTEs to get to the final result by joining and
anti-joining them in whatever way we require.

# Tip 3: Use sqlfmt

My third and final tip is to use an autoformatter for your SQL code.

As mentioned before, SQL is code and should be treated as such. Treat your SQL
like your Python and give it the attention and care it deserves. 

I don't always like how Python [Black](https://github.com/psf/black) looks but
consistency and other benefits far outweigh the cons (for me, at least).

A formatter I really like is [sqlfmt](https://github.com/tconbeer/sqlfmt). It prioritizes vertical space over horizontal space and was originally made for [dbt](https://discourse.getdbt.com/t/introducing-sqlfmt-an-auto-formatter-for-dbt-sql/3687), but I've grown to really like the style. 

It's the same with Black, first you hate it, then you love it. Give it some time. 

# Conclusion

Three tips for better SQL:

1. Start with a docstring
2. Use CTE's liberally
3. Use [sqlfmt](https://github.com/tconbeer/sqlfmt)

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
