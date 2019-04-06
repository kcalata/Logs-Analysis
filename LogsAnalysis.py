#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import os


# Returns the top articles of all time
def sort_articles():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("""select articles.title, count(*) as views
    from log, articles
    where log.status = '200 OK'
    and articles.slug = substr(log.path, 10)
    group by articles.title
    order by views desc
    limit 3;""")
    results = c.fetchall()
    db.close()
    return results


# Returns the top authors of all time
def sort_authors():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("""select authors.name, count(*) as views
    from log, authors, articles
    where log.status = '200 OK'
    and articles.slug = substr(log.path, 10)
    and authors.id = articles.author
    group by authors.name
    order by views desc;""")
    results = c.fetchall()
    db.close()
    return results


# Returns the days where more than 1% of requests lead to errors
def errors():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("""select errors.date,
    errors.err/errors.total * 100 as percentage
    from (select cast(time as date) as date,
    count(*) as total,
    cast(sum(cast(status != '200 OK' as int)) as float) as err
    from log group by date) as errors
    where errors.err/errors.total > 0.01;""")
    results = c.fetchall()
    db.close()
    return results


# Prints the results into an output file
def report():
    questions = ['1. What are the most popular three articles of all time?\n',
                 '2. Who are the most popular article authors of all time?\n',
                 '3. On which days did more than 1% of requests lead to '
                 'errors?\n']
    results = [sort_articles(), sort_authors(), errors()]
    f = open('LogsAnalysis.txt', 'w')
    f.write(questions[0])
    f.write('• \"' + str(results[0][0][0]) + '\" - ' + str(results[0][0][1])
            + ' views\n')
    f.write('• \"' + str(results[0][1][0]) + '\" - ' + str(results[0][1][1])
            + ' views\n')
    f.write('• \"' + str(results[0][2][0]) + '\" - ' + str(results[0][2][1])
            + ' views\n\n')
    f.write(questions[1])
    f.write('• ' + str(results[1][0][0]) + ' - ' + str(results[1][0][1])
            + ' views\n')
    f.write('• ' + str(results[1][1][0]) + ' - ' + str(results[1][1][1])
            + ' views\n')
    f.write('• ' + str(results[1][2][0]) + ' - ' + str(results[1][2][1])
            + ' views\n\n')
    f.write(questions[2])
    f.write('• ' + str(results[2][0][0]) + ' - ' + str(results[2][0][1])
            + '% errors\n')
    f.close()


if __name__ == "__main__":
    report()
