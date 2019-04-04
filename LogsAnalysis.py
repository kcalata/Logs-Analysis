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
