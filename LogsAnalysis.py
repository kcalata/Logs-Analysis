import psycopg2

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
print results
db.close()

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
print results
db.close()

db = psycopg2.connect("dbname=news")
c = db.cursor()
c.execute()"""select errors.date,
errors.err/errors.total as percentage
from (select cast(time as date) as date,
count(*) as total,
cast(sum(cast(status != '200 OK' as int)) as float) as err
from log group by date) as errors
where errors.err/errors.total > 0.01;""")
results = c.fetchall()
print results
db.close()
