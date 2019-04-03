import psychopg2

db = psycopg2.connect("dbname=news")
c = db.cursor()
c.execute('select path, count(*) as num from log group by oath order by num desc limit 3 offset 1;')
results = cursor.fetchall()
print results
db.close()
