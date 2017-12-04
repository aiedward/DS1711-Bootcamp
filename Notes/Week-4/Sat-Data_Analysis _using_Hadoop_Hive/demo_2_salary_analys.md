Hive Demo Step by Step ★★ - Salaries-Occupation Analysis 
---------------------
1. Create tables, load data
2. Query and analyze data
3. Add partitions
```sh
hadoop fs -mkdir -p /user/randy/demo/salary_analysis/sample_07
hadoop fs -mkdir -p /user/randy/demo/salary_analysis/sample_08
hadoop fs -copyFromLocal /tmp/sample_07 /user/randy/demo/salary_analysis/sample_07
hadoop fs -copyFromLocal /tmp/sample_08 /user/randy/demo/salary_analysis/sample_08
```

### Step 1 - Create tables
```sql
CREATE EXTERNAL TABLE sample_07(
code string,
description string,
total_emp int,
salary int)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS INPUTFORMAT
'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
'/user/randy/demo/salary_analysis/sample_07';
```

```sql
CREATE EXTERNAL TABLE sample_08(
code string,
description string,
total_emp int,
salary int)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS INPUTFORMAT
'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
'/user/randy/demo/salary_analysis/sample_08';
```

### Step 2 - analyze the data 
find one single record
```sql
SELECT * FROM sample_07 WHERE code = '11-1031';
```

Visualize results - list salary distribution
```sql
SELECT
description,
salary
FROM sample_07 
WHERE salary IS NOT NULL
ORDER BY salary DESC LIMIT 20;
```

Find out which makes more money in sample_08 than in sample_07, by difference percentage
```sql
SELECT
sample_08.description,
sample_08.salary,
sample_07.salary,
100* (sample_08.salary - sample_07.salary)/sample_07.salary as percentage
FROM sample_08
JOIN sample_07 ON sample_08.code = sample_07.code
where sample_08.salary > sample_07.salary
ORDER BY percentage DESC
LIMIT 20;
```


Find out the average total employee number and average salaries
```sql
SELECT
a.code,
a.description,
(a.total_emp + b.total_emp) /2 AS avg_total_emp,
(a.salary + b.salary) /2 AS avg_salary
FROM sample_07 a
JOIN sample_08 b ON a.code = b.code
WHERE a.salary IS NOT NULL AND b.salary IS NOT NULL
ORDER BY avg_salary DESC
LIMIT 20;
```


### Step 3 - add two files as partitions of a larger table

```sql
CREATE EXTERNAL TABLE sample_all(
code string,
description string,
total_emp int,
salary int)
partitioned by (year string)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS INPUTFORMAT
'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
'/user/randy/demo/salary_analysis/';
```

```sql
ALTER TABLE sample_all ADD IF NOT EXISTS PARTITION (year='07') LOCATION '/user/randy/demo/salary_analysis/sample_07';
ALTER TABLE sample_all ADD IF NOT EXISTS PARTITION (year='08') LOCATION '/user/randy/demo/salary_analysis/sample_08';
```

```sql
DESC FORMATTED sample_all;

SHOW PARTITIONS sample_all;
```

  
---------------------
#### ** Note: student to replace 'randy' in paths and db name with your own username