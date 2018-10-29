#!/usr/bin/env python3

import psycopg2

# Connect to postgres and instantiate cursor.
conn = psycopg2.connect("dbname=news user=postgres")
cur = conn.cursor()
