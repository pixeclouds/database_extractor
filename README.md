# database_extractor
A python script to dynamically extract data from a sqlite database

# Usage
- clone the repo to your machine
- run the script on the terminal using `py extract.py`
- the script take the database name/location as the first argument. This is arguement is compulsory
- it also takes a list of tables to be extracted from the database
- if no table is specified, the script extracts all the tables
- the extracted data is saved as a version of the db in a json file

# Example
```
 >>>   py extract school_db staff students
```
Here, school_database is the database name. The script will only extract data from the students and staff tables.
```
>>> Starting extraction...
>>> Message: Completed
>>> No of tables extracted: 2
>>> Data extract into: school_db-version-2023-05-01.json
```