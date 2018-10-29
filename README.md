# Analytics Report for 'news' Database.

This is the first assignment in the Full Stack Nano Degree from [Udacity](udacity.com).

It aims to answer the following questions about the provided data set.

1- What are the most popular three articles?

2- Who are the most popular article authors?

3- On which days did more than 1% of the requests fail?

## Installing requirements.

* Make sure you have `postgres` database installed and listening on `localhost:5432` (default config) or you can use [vagrant](https://classroom.udacity.com/nanodegrees/nd004/parts/51200cee-6bb3-4b55-b469-7d4dd9ad7765/modules/c57b57d4-29a8-4c5f-9bb8-5d53df3e48f4/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0?contentVersion=5.0.0&contentLocale=en-us).

* Download and unzip the data from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

* Import it by running `psql -d news -f newsdata.sql`.

* Make sure you have `python3` installed.

* Install `psycopg2` package by running `pip3 install psycopg2` (Will be used to connect to the database and execute queries).

## How to run it.

1- Clone and `cd` to the repo by running `git clone https://github.com/M-Dahab/fsnd_sql.git && cd fsnd_sql`.

2- Run the report by `python3 report.py` or simply `./report.py`.

3- It will print out three reports (See an example of the output in `example_output.txt`).

Thanks.