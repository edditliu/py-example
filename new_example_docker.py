#!/usr/bin/python3

import psycopg2

conn = psycopg2.connect("dbname='eddie' user='eddie' host='postgredb' password='eddie' port=5432")
with conn.cursor() as curs:
        for num in range(9,1000):
            id = num
            name = "robot_NO{}".format(num)
            sex = "男"
            if num % 2 == 0:
                sex = "女"
            curs.execute(f"update employee set name = '{name}' where id = {id} returning *")
            curs.execute(f"update employee set sex = '{sex}' where id = {id} returning *")
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

