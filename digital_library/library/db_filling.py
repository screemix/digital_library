import psycopg2

conn = psycopg2.connect(host='localhost',
    port=54320,
    dbname='db',
    user='user1')

conn.close()