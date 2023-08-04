import psycopg2
try:
    conn = psycopg2.connect("dbname='eddie' user='eddie' host='localhost' password=''")
except:
    print("I am unable to connect to the database")
with conn.cursor() as curs:
    for num in range(9,1000):
        id = num
        name = "robot{}".format(num)
        sex = "女"
        if num % 2 == 0:
            sex = "男"
        department_id = (num % 5) + 1 
        curs.execute(f"insert into employee (id, department_id, name, sex, birthdate, address, work_date, salary, level,title) VALUES ({id}, {department_id}, '{name}', '{sex}', '1998-11-11', 'Beijing', '2023-01-01', 7272, 'P1', 'developer')")
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