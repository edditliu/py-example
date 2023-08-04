import psycopg2
try:
    conn = psycopg2.connect(host='localhost',user='eddie',password='', dbname='eddie')
except:
    print("I can't connect to database")
with conn.cursor() as curs:
    for num in range(9,1000):
        id = num
        name = "new_robot{}".format(id)
        sex = "无"
        department_id = (num % 5) + 1
        curs.execute(f"insert into employee (id, department_id, name, sex, birthdate, address, work_date, salary, level,title) VALUES ({id}, {department_id}, '{name}', '{sex}', '2000-01-01', 'Beijing', '2023-07-30', 1111, 'P5', 'Tester')")
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