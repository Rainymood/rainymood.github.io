---
title: "Funny SQL bug because I thought `row_number()` started at 0"
date: 2022-10-23
tags:
- blog
- jekyll
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2022-10-23-funny-sql-bug-because-i-thought-row_number-started-at-0/thumbnail.png"
---

Can you spot the error in the docstring of this SQL snippet?

```sql
/* Aggregate features to arrays of size sequence_length (default 100) per user.
 * 
 * userid,  floor(row_number/100),     feat1, feat2, feat3
 * user1,   0                    ,     [...], [...], [...] 
 * user1,   1                    ,     [...], [...], [...]
 * user2,   0                    ,     [...], [...], [...]
 * 
 * Define bucket_num = floor(row_number/100). This maps row 1-100 to 0, row
 * 101-200 to 1, etc. Finally, ARRAY_AGG and GROUP BY the userid *and* the
 * bucket_num.
```

This is part of an SQL query that aggregates row-based data into feature arrays to use as input for our machine learning models. 

For every user we do a `row_number() over (partition by userid)` and we create a `bucket_num=floor(row_number/100)` that cuts the sequences for a particular user in slices of 100 observations. Finally we aggregate everything together with an `array_agg()`, `group by userid, bucket_num` and a `having count(*)=100`.

This is how I thought it was going to work:

| userid | row | row_number | floor(row_number/100) |
|--------|-----|------------|-----------------------|
| 1      | 1   | 0          | 0                     |
| 1      | 100 | 99         | 0                     |
| 1      | 101 | 100        | 1                     |

But when I started validating both datasets, the dataset with feature arrays was missing around 15% of users! For some reason aggregating the data from rows to arrays dropped some of the users. Weird.

So what do you do here? I debugged this with a colleague and we first tried out the most likely culprits: some awkward filters, some stray where clauses, and some other stuff. None of them really seemed to hit the mark. We did find one edge case that removed all users with fewer than 100 observations, because we do a `having count(*)=100` at the end of the group by. This explained some of the dropped users, but not enough to cover the whole difference.

Once we started looking at an individual user everything became clear. This is some data for a random user:

![](/../assets/2022-10-23-funny-sql-bug-because-i-thought-row_number-started-at-0/2022-10-23-08-56-41.png)


The first column is the userid, the second column is the `floor(row_number/100)` and the third column is a count of the rows in each bucket. To our surprise we see that **the first bucket only has 99 entries instead of the expected 100**. 

This allowed us to figure out what was happening: **Because the row number doesn't start at 0 but starts at 1, we filter out users that have at max 2 sequences**. 

For example: Imagine that a user has 150 rows to its name, then we map the first 99 rows to bucket 0 and the remaining 51 rows to bucket 1. Both of these sequences are smaller than the required length of 100 and get filtered out by the `having count(*)=100` clause. 

We filter out both rows and *this* drops the whole user!

Knowing this, the fix is straightforward. We just have to subtract 1 from the row number to make the first bucket contain 100 elements:

| userid | row | row_number-1 | floor((row_number-1)/100) |
|--------|-----|--------------|-----------------------|
| 1      | 1   | 0            | 0                     |
| 1      | ..  | ..           | ..                    |
| 1      | 100 | 99           | 0                     |
| 1      | 101 | 100          | 1                     |

That way, we do not filter users with only 2 sequences because their first sequence, now with exactly 100 observations, stays in the dataset. Problem solved!

Here is the corrected SQL snippet. The only difference is that we subtract 1 from the row number.

```sql
/* Aggregate features to arrays of size sequence_length (default 100) per user.
 * 
 * userid,  floor((row_number-1)/100),     feat1, feat2, feat3
 * user1,   0                        ,     [...], [...], [...] 
 * user1,   1                        ,     [...], [...], [...]
 * user2,   0                        ,     [...], [...], [...]
 * 
 * Define bucket_num = floor((row_number-1)/100). This maps row 1-100 to 0, row
 * 101-200 to 1, etc. Finally, ARRAY_AGG and GROUP BY the userid *and* the
 * bucket_num.
```

My lesson learned here is that if you fiddle with things like row numbers, make sure to check whether they start at zero or one.