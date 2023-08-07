---
title: "Unveiling a hidden gem: Achieving a 10x speedup on an AWS Athena SQL query with ZERO results on Google"
date: 2023-08-06
tags:
- sql
- aws 
- athena
- work
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2023-08-06-unveiling-a-hidden-gem-achieving-a-10x-speedup-on-an-aws-athena-sql-query-with-zero-results-on-google/2023-08-06-13-34-23.png"

---

Ever since AWS moved their Athena engine to [version 3](https://docs.aws.amazon.com/athena/latest/ug/engine-versions-reference-0003.html) weird things started happening to us. 

This query that used to run under 3 minutes now times out after 45 minutes. What the hell?

![](/../assets/2023-08-06-unveiling-a-hidden-gem-achieving-a-10x-speedup-on-an-aws-athena-sql-query-with-zero-results-on-google/2023-08-06-13-39-53.png)

After trying to debug this query unsuccessfully for hours, we decided to contact AWS Support directly and this is what they said (paraphrased):

> AWS Support: So uhmmm, maybe like, yeah, try... adding this to your query somewhere: `@{rule_based_join_reorder ='false'}`?
>
> AWS Support: ...
>
> AWS Support: We just like added this as an experimental feature but forgot to document it lol xoxo aws

If you google this you get literally **zero results**:

![](/../assets/2023-08-06-unveiling-a-hidden-gem-achieving-a-10x-speedup-on-an-aws-athena-sql-query-with-zero-results-on-google/2023-08-06-16-28-35.png)

(Update 2023-08-07: My blog post is now the first hit, hehe)

It feels like I'm in possession of this forbidden jutsu that no one else knows and it feels great. Anyway, you can guess what we tried out next:

![](/../assets/2023-08-06-unveiling-a-hidden-gem-achieving-a-10x-speedup-on-an-aws-athena-sql-query-with-zero-results-on-google/2023-08-06-16-17-58.png)

```sql
@{rule_based_join_reorder ='false'}
WITH pupils as (
    SELECT pupilid
        ...
        -- very long and complex sql query here
```

![](/../assets/2023-08-06-unveiling-a-hidden-gem-achieving-a-10x-speedup-on-an-aws-athena-sql-query-with-zero-results-on-google/2023-08-06-16-18-05.png)

What just happened here exactly? I had no clue so I asked ChatGPT:

> Me: Dear ChatGPT, What does @{rule_based_join_reorder ='false'} do?
>
> ChatGPT:  In SQL Server, the rule_based_join_reorder option is used to control the query optimizer's behavior for reordering joins in query execution plans. 
>
> ... (more bla bla bla)

It turns out that there is this undocumented setting in AWS that allows us to disable the rule based join reordering. The heuristics used to order the joins turned out to be very inefficient for our specific query, resulting in the huge speedup after disabling it.

In other words: haha athena go brrrrrr

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
    