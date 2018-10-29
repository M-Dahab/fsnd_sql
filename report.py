#!/usr/bin/env python3

import psycopg2

# Connect to postgres and instantiate cursor.
conn = psycopg2.connect("dbname=news user=postgres")
cur = conn.cursor()


# Print the first report (The most popular three articles viewed).
cur.execute('''
  SELECT articles.title, COUNT(log.id) as views
    FROM articles, log
    WHERE log.path = concat('/article/', articles.slug)
    GROUP BY articles.title
    ORDER BY views desc
    LIMIT 3;
''')

print('\n\t\t# REPORT 1\n')
print('\nThe most popular three articles viewed are:\n')

for idx, row in enumerate(cur.fetchall()):
    print('%d- %s — %d views.\n' % (idx + 1, row[0], row[1]))


