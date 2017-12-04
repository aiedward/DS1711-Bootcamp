Hive Demo Step by Step ★ - Beginner practice
---------------------
1. Create tables, load data
2. Query and analyze data
3. Add partitions

### Step 1. create a text file in local system
```sh
mkdir -p /home/randy/demo/students_tb/students/
vi /home/randy/demo/students_tb/students/students.txt
```

### Step 2. paste below rows into the file
```sh
1,Nic,Raboy,Merced,California
2,Jane,Doe,Newark,New York
3,John,Lee,Las Vegas,Nevada
4,Maria,Campos,Modesto,California
```

### Step 3. Create an empty table for students
```sql
CREATE TABLE students(id INT, first_name STRING, last_name STRING, city STRING, state STRING) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';
```

### Step 4. Load the text file into this table

```sql
LOAD DATA LOCAL INPATH '/home/randy/demo/students_tb/students/students.txt' OVERWRITE INTO TABLE students;
```

### Step 5. query this table to validate it
```sql
SELECT * FROM students;
```
  
---------------------
#### ** Note: student to replace 'randy' in paths and db name with your own username