Hive Demo Step by Step ★★★ - Social Media Data Operation and Analysis
---------------------
In this demo, we will practice the following with Twitter log data:
1. Load a data file into a Hive table
2. Create a table using RCFormat
3. Query tables
4. Managed tables vs external tables
5. ORC format
6. PARTITIONED a Table



### Step 1. Let’s load a data file into a Hive table.
```sh
mkdir -p /home/randy/demo/twitter/
cd /home/randy/demo/twitter/
wget http://hortonassets.s3.amazonaws.com/tutorial/hive/Twitterdata.txt
```
```sh
hadoop fs -mkdir -p /user/randy/demo/twitter/
hadoop fs -copyFromLocal /home/randy/demo/twitter/Twitterdata.txt /user/randy/demo/twitter/
```

```sql
USE randy_db;
CREATE TABLE IF NOT EXISTS TwitterExampleManaged(
        tweetId BIGINT,
        username STRING,
        txt STRING,
        CreatedAt STRING,
        profileLocation STRING,
        favc BIGINT,
        retweet STRING,
        retcount BIGINT,
        followerscount BIGINT
        )
COMMENT 'This is the Twitter streaming data'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE;

LOAD DATA INPATH '/user/randy/demo/twitter/' OVERWRITE INTO TABLE TwitterExampleManaged;

SELECT * FROM TwitterExampleManaged LIMIT 100;

```
### Step 2. Let’s create a table using RCfile format
Record Columnar(RC) format determines how to store relational tables on distributed computer clusters.
With this format, you can get the advantages of a columnar format over row format of a record.
```sql
CREATE TABLE TwitterExampleRCtable(
        tweetId BIGINT, username STRING,
        txt STRING, CreatedAt STRING,
        profileLocation STRING COMMENT 'Location of user',
        favc BIGINT,retweet STRING,retcount BIGINT,followerscount BIGINT)
COMMENT 'This is the Twitter streaming data'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS RCFILE;

INSERT OVERWRITE TABLE TwitterExampleRCtable select * from  TwitterExampleManaged;
```
### Step 3. Let’s query the table we just created - find top 10 countries who tweeted most
```sql
SELECT profileLocation, COUNT(txt) as count1
FROM TwitterExampleRCtable
GROUP BY profileLocation
ORDER BY count1 desc limit 10;
```
### Step 4. Let’s look at Managed tables vs External tables
Managed tables are created by default with CREATE TABLE statements, whereas
External tables are used when you want your tables to point to data files in place, therefore it has to be a folder you point to.
when you drop a Managed table, it deletes the metadata, and it also deletes the data.
When you drop an External table, it only deletes the metadata.
By creating a managed table the file you load in is moved to /apps/hive/warehouse that means that the data is controlled by hive.
Whereas the external tables points to the /tmp/admin directory in which we put the Twitterdata.txt.
If we run the sample query you should see the data from this file.
```sh
hadoop fs -mkdir -p /user/randy/demo/twitter_external/
hadoop fs -copyFromLocal /home/randy/demo/twitter/Twitterdata.txt  /user/randy/demo/twitter_external/
```
```sql
CREATE EXTERNAL TABLE IF NOT EXISTS TwitterExampleExternal(
        tweetId BIGINT, username STRING,
        txt STRING, CreatedAt STRING,
        profileLocation STRING,
        favc BIGINT,retweet STRING,retcount BIGINT,followerscount BIGINT)
COMMENT 'This is the Twitter streaming data'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE
location '/user/randy/demo/twitter_external/';

describe formatted TwitterExampleManaged;
describe formatted TwitterExampleExternal;
```
### Step 5. Hive ORC File format.
Optimized Row Columnar (ORC) File format is used as it further compresses data files.
It could result in a small performance loss in writing, but there will be huge performance gain in reading.
```sql
CREATE TABLE TwitterExampleORC(
    tweetId BIGINT, username STRING,
    txt STRING, CreatedAt STRING,
    profileLocation STRING COMMENT 'Location of user',
    favc INT,retweet STRING,retcount INT,followerscount INT)
COMMENT 'This is the Twitter streaming data'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS ORC tblproperties ("orc.compress"="ZLIB");
```
### Step 6. Let’s create a PARTITIONED Table and load data into
Partitions are horizontal slices of data which allow large sets of data to be segmented into more manageable blocks.
```sql
CREATE TABLE TwitterExamplePartitioned(
      tweetId BIGINT,
      username STRING,
      txt STRING,
      favc BIGINT,
      retweet STRING,
      retcount BIGINT,
      followerscount BIGINT
      )
COMMENT 'This is the Twitter streaming data'
PARTITIONED BY(CreatedAt STRING, profileLocation STRING)
ROW FORMAT DELIMITED FIELDS
TERMINATED BY '\t' STORED AS TEXTFILE;

INSERT OVERWRITE TABLE TwitterExamplePartitioned
PARTITION (CreatedAt="2015_12_12_14",profileLocation="Chicago")
SELECT tweetId,username,txt,favc,retweet,retcount,followerscount
FROM TwitterExampleExternal
where profileLocation='Chicago' limit 100;

INSERT OVERWRITE TABLE TwitterExamplePartitioned
PARTITION (CreatedAt="2015_12_12_14",profileLocation="Bay Area, CA")
SELECT tweetId,username,txt,favc,retweet,retcount,followerscount
FROM TwitterExampleExternal
where profileLocation='Bay Area, CA' limit 100;


SELECT profileLocation, SUM(followerscount) as followerscounts
FROM TwitterExamplePartitioned
GROUP BY profileLocation
ORDER BY followerscounts DESC;

ALTER TABLE TwitterExamplePartitioned DROP IF EXISTS PARTITION (CreatedAt="2015_12_12_14",profileLocation="Bay Area, CA");
```

### Step 7. Hive with Spark SQL
```scala
import org.apache.spark.sql.hive.HiveContext
val sc = new SparkContext(new SparkConf().setAppName(this.getClass.getName))
val hiveContext = new HiveContext(sc)

val createTbSql = """
CREATE EXTERNAL TABLE IF NOT EXISTS randy_db.TwitterExampleSpark(
        tweetId BIGINT, username STRING,
        txt STRING, CreatedAt STRING,
        profileLocation STRING,
        favc BIGINT,retweet STRING,retcount BIGINT,followerscount BIGINT)
COMMENT 'This is the Twitter streaming data created in Spark'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE
location '/user/randy/demo/twitter_external/'
"""
val query = """
SELECT * FROM randy_db.TwitterExampleSpark LIMIT 20
"""

hiveContext.sql(createTbSql)
val results = hiveContext.sql(query)

results.show
```

  
---------------------
#### ** Note: student to replace 'randy' in paths and db name with your own username