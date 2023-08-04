import psycopg2
try:
    conn = psycopg2.connect(host='localhost',user='eddie', password='',dbname='eddie')
except:
    print("failed to connect to database")
with conn.cursor() as curs:
    for num in range(1001,2000):
        id = num
        curs.execute(f"delete from employee where id = {num} returning *")
        curs.execute("commit")
    try:
        curs.execute("select * from employee")
        pg_rows = curs.fetchall()

        for pg_row in pg_rows:
            for index in range(0,11):
                print(pg_row[index], end='\t| ')
            print()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)