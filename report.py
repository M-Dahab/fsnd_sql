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


# Print the second report (The most popular article authors).
cur.execute('''
  SELECT authors.name, COUNT(log.id) as views
    FROM authors, articles, log
    WHERE log.path = concat('/article/', articles.slug)
        AND articles.author = authors.id
    GROUP BY authors.name
    ORDER BY views desc;
''')
print('\n\t\t# REPORT 2\n')
print('\n\nThe most popular article authors are:\n')

for idx, row in enumerate(cur.fetchall()):
    print('%d- %s — %d views.\n' % (idx + 1, row[0], row[1]))


# Print the third report
# (On which days did more than 1% of requests lead to errors?).
cur.execute('''
  select to_char(date, 'YYYY-MM-DD'), errors
    from (
      select date_trunc('day', time) as date,
        round(
          (count(case when status = '404 NOT FOUND' then 1 end)::float /
          count(id) * 100)::numeric,
          2
        ) as errors
      from log
      group by date
      order by errors desc
    ) as errors_report
    where errors > 1;
''')
print('\n\t\t# REPORT 3\n')
print('\n\nDays with more than 1% error rate are:\n')

for idx, row in enumerate(cur.fetchall()):
    print(
      '%d- %s — %s%% of requests failed.\n' % (idx + 1, str(row[0]), row[1])
    )
