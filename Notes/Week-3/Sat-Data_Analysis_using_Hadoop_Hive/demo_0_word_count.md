Hive Demo Step by Step - Word Count
---------------------
## Part I:  In Hive
#### 0_a) prep files: create directories, download files, copy files to HDFS
```sh
mkdir -p /home/randy/demo/wordcount
cd /home/randy/demo/wordcount
wget http://www.gutenberg.org/cache/epub/1342/pg1342.txt
wget http://www.gutenberg.org/cache/epub/4300/pg4300.txt
wget http://www.gutenberg.org/cache/epub/132/pg132.txt
wget http://www.gutenberg.org/cache/epub/1661/pg1661.txt
wget http://www.gutenberg.org/cache/epub/972/pg972.txt
wget http://www.gutenberg.org/cache/epub/19699/pg19699.txt
hadoop fs -rm -r /user/randy/demo/hive/wordcount/input/big/
hadoop fs -mkdir -p /user/randy/demo/hive/wordcount/input/big/
hadoop fs -copyFromLocal /home/randy/demo/wordcount/pg*.txt /user/randy/demo/hive/wordcount/input/big/
```

Hive queries for Word Count
####  0_b) pre clean-up: get a clean state so we can continue
```sql
CREATE DATABASE IF NOT EXISTS randy_db;
USE randy_db;
DROP TABLE IF EXISTS doc;
```
#### 1) create table to load whole file
```sql
CREATE TABLE doc(text STRING)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\n' STORED AS textfile
LOCATION '/user/randy/demo/hive/wordcount/input/big';
```
#### 2) wordCount in single line
```sql
SELECT word, COUNT(*) AS cnt FROM doc LATERAL VIEW explode(split(text, ' ')) lTable AS word GROUP BY word ORDER BY cnt DESC LIMIT 200;
```

## Part II: In MapReduce
#### 3) vs MapReduce?
```sh
hadoop fs -rm -R /user/randy/demo/mapreduce/wordcount/output
hadoop jar /usr/hdp/2.5.3.0-37/hadoop-mapreduce/hadoop-mapreduce-examples.jar \
          wordcount /user/randy/demo/hive/wordcount/input/big \
          /user/randy/demo/mapreduce/wordcount/output
```
  
---------------------
#### ** Note: student to replace 'randy' in paths and db name with your own username

