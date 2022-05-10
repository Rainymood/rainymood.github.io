---
title: "Show your work: Writing gnarly SQL queries"
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
  teaser: "/../assets/2022-04-29-show-your-work-create-testset-automation/thumbnail3.png"
---

Today I wrote this SQL query

![](/../assets/2022-05-10-show-your-work-sql/2022-05-10-16-34-17.png)

It starts with a small docstring.

I like to treat my SQL like I like my code, well documented. Some of my
colleagues disagree and think that the code should speak for itself, but I
always greatly appreciate a good docstring. 

```sql
/* Create-repopulation-61688-for-default-difficultiers.sql

Creates the table that is needed for continuous calibration (CC). We create this
table because we want to revert all previously continuously calibrated
difficulties from 1-10-2012 to 3-5-2022 because of the irtfit issue.

Revert all events that:
    1. Had no event before that date, but had an event after
    2. Had a default difficulty event before that date and an event after
*/
```

Then we create the subtable `calibrated_exercises` which contains the exercises
(by their `originalexerciseid`) that we need to consider.

```sql
with calibrated_exercises as (
    SELECT distinct originalexerciseid
    FROM "prod_calibration_warehouse"."exercise_calibrations_succeeded" ecs
    where 1=1
        AND coalesce(eventdateutc, calibrationdate) > date('2021-10-01')
        -- we only want to overwrite continuous calibrations, not default difficulties
        AND source like '%continuous%'
), 
```

Then we create two tables `previous_events` which contains all the calibration events prior to `2021-10-01`. 

The last known date with "healthy" calibrations. 

```sql
previous_events as (
    SELECT
        * 
        , row_number() over (partition by originalexerciseid order by coalesce(ecs.eventdateutc, ecs.calibrationdate) desc) as rank
    FROM "prod_calibration_warehouse"."exercise_calibrations_succeeded" ecs
    WHERE coalesce(ecs.eventdateutc, ecs.calibrationdate) <= date('2021-10-01') 
), 
```

The second table is called the `after_events`. 

```sql
after_events as (
    SELECT
        * 
        , row_number() over (partition by originalexerciseid order by coalesce(ecs.eventdateutc, ecs.calibrationdate) desc) as rank
    FROM "prod_calibration_warehouse"."exercise_calibrations_succeeded" ecs
    WHERE coalesce(ecs.eventdateutc, ecs.calibrationdate) > date('2021-10-01') 
)
```

And finally we take the union between the following to two tables

The first one is this

```sql
-- Events with before no after yes => we consider these default difficulties and take the last known difficulty
SELECT 
    ce.originalexerciseid as originalexerciseid
    , ae.difficulty as difficulty
    , ae.difficultynonadaptive as difficultynonadaptive
    , ae.difficultyadaptive as difficultyadaptive
    , NULL as irtfit
    , NULL as irtfitnonadaptive
    , NULL as irtfitadaptive
    , NULL as calibrationdate
    , NULL as numberofexercises
    , '{"difficulty": "repopulation-61688", "difficultynonadaptive":"repopulation-61688", "difficultyadaptive":"repopulation-61688"}' as source
FROM calibrated_exercises ce
LEFT JOIN previous_events pe ON ce.originalexerciseid = pe.originalexerciseid 
JOIN after_events ae on ce.originalexerciseid = ae.originalexerciseid
WHERE 1=1
    -- only take the last known difficulty
    AND ae.rank = 1
    -- anti-join to exclude exercises in previous events
    AND pe.originalexerciseid is null
```

Which we union

```sql
...

UNION

...
```

With the following table 

```sql
-- Events with (a default difficulty) before yes and after yes => we consider these default difficulties
SELECT 
    ce.originalexerciseid as originalexerciseid
    , ae.difficulty as difficulty
    , ae.difficultynonadaptive as difficultynonadaptive
    , ae.difficultyadaptive as difficultyadaptive
    , NULL as irtfit
    , NULL as irtfitnonadaptive
    , NULL as irtfitadaptive
    , NULL as calibrationdate
    , NULL as numberofexercises
    , '{"difficulty": "repopulation-61688", "difficultynonadaptive":"repopulation-61688", "difficultyadaptive":"repopulation-61688"}' as source
FROM calibrated_exercises ce
-- LEFT JOIN previous_events pe ON ce.originalexerciseid = pe.originalexerciseid
JOIN after_events ae on ce.originalexerciseid = ae.originalexerciseid
WHERE 1=1
    -- only take the last known difficulty
    AND ae.rank = 1
    -- Consider previous exercises that only had a DD in both contexts as difficulties we have to reset (source like '%Default%' is not covering)
    AND EXISTS (
        SELECT * 
        FROM previous_events pe 
        WHERE 1=1
            AND ce.originalexerciseid = pe.originalexerciseid
            -- only take exercises with a DD as their last event in previous_events
            AND pe.rank = 1 
            AND pe.source like '%Default%'
            AND pe.irtfitadaptive is null
            AND pe.irtfitnonadaptive is null
        )
```

# Takeaways

* Subtables/CTEs are your friend
* Document your SQL code like you would your normal code
* These queries might seems complex, but if you build them up slowly they become easy to understand

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
  <label for="mce-EMAIL">Liked this article and want to hear more? Join 40+ others and subscribe!</label>
  <input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>
    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_92fe86c389878585bc87837e8_50543deff9" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>
<!--End mc_embed_signup-->
