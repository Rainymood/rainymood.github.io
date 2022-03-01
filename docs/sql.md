# SQL

## `and (ha.exerciseinlessonid is null or not eil.exam)`

We have to include `ha.exerciseinlessonid` because we join on that key. If we
don't do this, then these keys where this value is `null` will be lost in the
join. Because we join on this key to filter on it later.

```sql
SELECT ...
FROM ...ha
	LEFT JOIN  ... eil ON ha.exerciseinlessonid = eil.exerciseinlessonid
WHERE 1 = 1
	and (ha.exerciseinlessonid is null or not eil.exam)
```

## How to get the difficulties

```sql
SELECT ...,
   if (
         ha.exerciseinlessonid is null,
         e.difficultyadaptive,
         e.difficultynonadaptive
   ) as difficulty,
FROM ... ha
   LEFT JOIN ... e ON e.exerciseid = ha.exerciseid
```