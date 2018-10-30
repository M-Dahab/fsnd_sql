# Analytics Report for 'news' Database.

This is the first assignment in the Full Stack Nano Degree from [Udacity](udacity.com).

It aims to answer the following questions about the provided data set.

1- What are the most popular three articles?

2- Who are the most popular article authors?

3- On which days did more than 1% of the requests fail?

## Dependencies.

1- `python3`.

2- `psycopg2` package.

3- `postgres` database.

## Preparing the project.

* Install and start `postgres` and make sure It's listening on `localhost:5432` (default config).

* Download and unzip the data from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

* Import it by running `psql -d news -f newsdata.sql`.

* Make sure you have `python3` installed.

* Install `psycopg2` package by running `pip3 install psycopg2` (Will be used to connect to the database and execute queries).

## How to run it.

1- Clone and `cd` to the repo by running `git clone https://github.com/M-Dahab/fsnd_sql.git && cd fsnd_sql`.

2- Run the report by `python3 report.py` or simply `./report.py`.

3- It will print out three reports (See an example of the output in `example_output.txt`).

Thanks.