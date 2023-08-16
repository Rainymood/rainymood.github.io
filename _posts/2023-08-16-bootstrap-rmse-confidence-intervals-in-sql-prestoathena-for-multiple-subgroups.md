---
title: "Bootstrap RMSE Confidence Intervals in SQL (Presto/Athena) for multiple subgroups"
date: 2023-08-16
tags:
- sql
- aws 
- athena
- work
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2023-08-16-bootstrap-rmse-confidence-intervals-in-sql-prestoathena-for-multiple-subgroups/2023-08-16-08-38-23.png"
---

In this blog post I want to show you how to calculate approximate confidence intervals in SQL (Presto/Athena dialect) using [bootstrapping](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)), specifically for the Root Mean Squared Error (RMSE) *and* in multiple subgroups.

This post builds on top of this blog post, [Bootstrap Confidence Intervals in SQL for PostgreSQL and BigQuery](https://jdlm.info/articles/2023/06/11/bootstrap-confidence-intervals-sql-postgresql-bigquery.html), but extends it for multiple subgroups.


# Final result

Starting from some data with columns `(category, label, error)` where `err` is the prediction error calculated as correct minus your predicted probability (`err = correct - prediction`)

| category | label | err |
|----------|-------|-----|
| 0        | 0     | 1   |
| 0        | 0     | 2   |
| 0        | 0     | 3   |
| 0        | 1     | 11  |
| 0        | 1     | 12  |
| 0        | 1     | 13  |
| 0        | 1     | 14  |
| 1        | 0     | 100 |
| 1        | 0     | 200 |
| 1        | 0     | 300 |
| 1        | 0     | 400 |
| 1        | 0     | 500 |

The query calculates the bootstrapped 95% RMSE CI 

| category | label | rmse_lo | rmse   | rmse_hi |
|----------|-------|---------|--------|---------|
| 0        | 0     | 1.0     | 2.16   | 3.0     |
| 0        | 1     | 11.53   | 12.55  | 13.28   |
| 1        | 0     | 223.61  | 331.66 | 397.49  |

# How

Let's jump right in!

```sql
with labelled as (
	select *
	from (
        values (0, 0,1),
            (0, 0, 2),
            (0, 0, 3),
            (0, 1, 11),
            (0, 1, 12),
            (0, 1, 13),
            (0, 1, 14),
            (1, 0, 100),
            (1, 0, 200),
            (1, 0, 300),
            (1, 0, 400),
            (1, 0, 500)
		) as t(category, label, err)
),
bootstrap_indexes as (
SELECT bootstrap_index
	FROM (SELECT sequence(1, 10) as d)
	CROSS JOIN UNNEST (d) as t(bootstrap_index)
),
bootstrap_data AS (
  SELECT 
        category,
        label,
        err,
        ROW_NUMBER() OVER(partition by category, label) - 1 AS data_index
  FROM labelled
),
bootstrap_amounts as (
    select
        category,
        label,
        count(*) as amount
    from bootstrap_data
    group by category, label
),
bootstrap_map AS (
  SELECT 
    d.category,
    d.label,
    a.amount,
    cast(floor(random() * a.amount) as int) AS sampled_index,
    bootstrap_index
  FROM bootstrap_data d
  JOIN bootstrap_amounts a 
    on a.category = d.category 
    and a.label = d.label
  JOIN bootstrap_indexes ON TRUE
), 
bootstrap AS (
  SELECT 
    m.category,
    m.label,
    bootstrap_index,
    err
  FROM bootstrap_map m
  JOIN bootstrap_data d 
    on m.category = d.category 
    and m.label = d.label 
    and m.sampled_index = d.data_index
),
bootstrap_aggregated AS (
  SELECT 
    category,
    label,
    bootstrap_index,
    sqrt(avg(pow(err, 2))) as rmse
  FROM bootstrap
  group by category, label, bootstrap_index
),
bootstrap_ci AS (
  SELECT
    category,
    label,
    approx_percentile(rmse, 0.025) as rmse_lo,
    approx_percentile(rmse, 0.975) as rmse_hi
  FROM bootstrap_aggregated
  group by category, label
),
sample AS (
  SELECT 
    category,
    label,
    sqrt(avg(pow(err, 2))) AS rmse_avg
  FROM labelled
  group by category, label
)
SELECT 
    s.category,
    s.label,
    round(rmse_lo,2) as rmse_lo,
    round(rmse_avg, 2) as rmse,
    round(rmse_hi, 2) as rmse_hi
FROM sample s
JOIN bootstrap_ci c 
    on s.category = c.category 
    and s.label = c.label
order by category, label
```

Let's break this query down one CTE at a time.

`labelled` creates our data.

| category | label | err |
|----------|-------|-----|
| 0        | 0     | 1   |
| 0        | 0     | 2   |
| 0        | 0     | 3   |
| ...      | ..    | ..  |
| 1        | 0     | 500 |

`bootstrap_indexes` enumerates the bootstrap samples you want to do.

| bootstrap_index |
|-----------------|
| 1               |
| ...             |
| 9               |
| 10              |

`bootstrap_data` enumerates each row in each category/label subgroup. We need this query because we are going to use `data_index` to resample.

| category | label | err | data_index |
|----------|-------|-----|------------|
| 0        | 1     | 11  | 0          |
| 0        | 1     | 12  | 1          |
| 0        | 1     | 13  | 2          |
| 0        | 1     | 14  | 3          |
| 0        | 0     | 1   | 0          |
| 0        | 0     | 2   | 1          |
| 0        | 0     | 3   | 2          |
| 1        | 0     | 100 | 0          |
| 1        | 0     | 200 | 1          |
| 1        | 0     | 300 | 2          |
| 1        | 0     | 400 | 3          |
| 1        | 0     | 500 | 4          |

`bootstrap_amounts` contains the number of rows in each category/label subgroup. 

| category | label | amount |
|----------|-------|--------|
| 0        | 1     | 4      |
| 0        | 0     | 3      |
| 1        | 0     | 5      |

`bootstrap_map` performs the resampling with replacement. 

For each category/label subgroup we take a full sample by sampling random integers in the
range of `amount` (which differs per subgroup).

The `JOIN bootstrap_indexes ON TRUE` gives the full cartesian product of the bootstrap and data indexes, in this case we have 10 bootstrap samples and 12 observations which results in 120 rows.

| category | label | amount | sampled_index | bootstrap_index |
|----------|-------|--------|---------------|-----------------|
| 0        | 0     | 3      | 0             | 1               |
| 0        | 0     | 3      | 2             | 1               |
| 0        | 0     | 3      | 1             | 1               |
| 0        | 1     | 4      | 3             | 1               |
| ..       | ..    | ..     | ..            | ..              |
| 0        | 1     | 3      | 1             | 9               |

`bootstrap` joins back the actual data instead of the sampled index. This `bootstrap` table now contains 10 full new samples we bootstrapped!

| category | label | bootstrap_index | err |
|----------|-------|-----------------|-----|
| 0        | 0     | 1               | 1   |
| 0        | 0     | 1               | 1   |
| 0        | 0     | 1               | 1   |
| 0        | 1     | 1               | 12  |
| ..       | ..    | ..              | ..  |
| 0        | 1     | 9               | 13  |

`bootstrap_aggregated` calculates the RMSE for each individual sample (i.e.
`bootstrap_index`). 

| category | label | bootstrap_index | rmse   |
|----------|-------|-----------------|--------|
| 0        | 0     | 2               | 3.0    |
| 0        | 0     | 4               | 2.71   |
| 0        | 0     | 5               | 2.71   |
| 0        | 0     | 9               | 1.41   |
| 0        | 0     | 1               | 2.16   |
| 0        | 0     | 6               | 2.52   |
| 0        | 0     | 8               | 2.16   |
| 0        | 0     | 10              | 2.16   |
| 1        | 0     | 4               | 428.95 |
| 0        | 1     | 2               | 13.04  |
| ..       | ..    | ..              | ..     |
| 1        | 0     | 10              | 240.83 |

`bootstrap_ci` uses `approx_percentile()` to find the percentiles of the empirical bootstrap distribution that we need.

| category | label | rmse_lo | rmse_hi |
|----------|-------|---------|---------|
| 0        | 0     | 1.41    | 2.52    |
| 1        | 0     | 249.0   | 500.0   |
| 0        | 1     | 11.51   | 13.53   |

`sample` computes the **actual** observed RMSE in the category/label subgroups.
Note that I calculate the RMSE from the actual observations here and not the
bootstrapped RMSE!

| category | label | rmse_avg |
|----------|-------|----------|
| 0        | 1     | 12.55    |
| 0        | 0     | 2.16     |
| 1        | 0     | 331.66   |

Finally, we can combine everything together: the bootstrapped RMSE 95% CI and the observed RMSE for every category/label subgroup.

| category | label | rmse_lo | rmse   | rmse_hi |
|----------|-------|---------|--------|---------|
| 0        | 0     | 1.41    | 2.16   | 2.71    |
| 0        | 1     | 11.51   | 12.55  | 13.51   |
| 1        | 0     | 249.0   | 331.66 | 428.95  |

# Optional: Simple case (without subgroups)

For the simple case (without subgroups) I want to refer you back to the original [blog post](https://jdlm.info/articles/2023/06/11/bootstrap-confidence-intervals-sql-postgresql-bigquery.html).

For completeness I'll add it in. Imagine you have a table with prediction errors like this:

| err |
|-----|
| 100 |
| 200 |
| 300 |
| 400 |
| 500 |

And you want to turn it into this (where `rmse_lo` and `rmse_hi` are bootstrapped RMSE 95% CI.):

| rmse_lo | rmse   | rmse_hi |
|---------|--------|---------|
| 279.28  | 331.66 | 426.61  |

```sql
with labelled as (
	select *
	from (
			values 
				(100),
				(200),
				(300),
				(400),
				(500)
		) as t(err)
),
bootstrap_indexes as (
SELECT bootstrap_index
	FROM (SELECT sequence(1, 10) as d)
	CROSS JOIN UNNEST (d) as t(bootstrap_index)
),
bootstrap_data AS (
  SELECT 
        err,
        ROW_NUMBER() OVER() - 1 AS data_index
  FROM labelled
),
bootstrap_map AS (
  SELECT 
    cast(floor(random() * (select count(data_index) from bootstrap_data)) as int) AS sampled_index,
    bootstrap_index
  FROM bootstrap_data d
  JOIN bootstrap_indexes ON TRUE
), 
bootstrap AS (
  SELECT 
    bootstrap_index,
    err
  FROM bootstrap_map m
  JOIN bootstrap_data d on m.sampled_index = d.data_index
),
bootstrap_aggregated AS (
  SELECT 
    bootstrap_index,
    sqrt(avg(pow(err, 2))) as rmse
  FROM bootstrap 
  group by bootstrap_index
),
bootstrap_ci AS (
  SELECT
    approx_percentile(rmse, 0.025) as rmse_lo,
    approx_percentile(rmse, 0.975) as rmse_hi
  FROM bootstrap_aggregated
),
sample AS (
  SELECT 
    sqrt(avg(pow(err, 2))) AS rmse_avg
  FROM labelled
)
SELECT 
    round(rmse_lo,2) as rmse_lo,
    round(rmse_avg, 2) as rmse,
    round(rmse_hi, 2) as rmse_hi
FROM sample s
JOIN bootstrap_ci on TRUE
```

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
    