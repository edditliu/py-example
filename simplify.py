import psycopg2
try:
    conn = psycopg2.connect(host='localhost',user='eddie',password='',dbname='eddie')
except:
    print("Failed to connect to database")
with conn.cursor() as curs:
    def change_id(num):
        curs.execute(f"select * from employee where id={num}")
        info = curs.fetchall()
        print(" id     | department_id | name  | sex   | birthdate             | address       | work_date             | salary| level |  title        | memo")
        print("--------+---------------+-------+-------+-----------------------+---------------+-----------------------+-------+-------+---------------+-----")
        for e_info in info:
            for index in range(0,11):
                print(e_info[index],end='\t| ')
            print()
    def new_d_id(new_department_id):
            curs.execute(f"update employee set department_id = '{new_department_id}' where id = {num} returning *")
            curs.execute("commit")
    def new_n(new_name):
            curs.execute(f"update employee set name = '{new_name}' where id = {num} returning *")
            curs.execute("commit")
    def new_x(new_sex):
            curs.execute(f"update employee set sex = '{new_sex}' where id = {num} returning *")
            curs.execute("commit")
    def new_bd(new_birthdate):
            curs.execute(f"update employee set birthdate = '{new_birthdate}' where id = {num} returning *")
            curs.execute("commit")
    def new_ad(new_address):
            curs.execute(f"update employee set address = '{new_address}' where id = {num} returning *")
            curs.execute("commit")
    def new_wd(new_work_date):
            curs.execute(f"update employee set work_date = '{new_work_date}' where id = {num} returning *")
            curs.execute("commit")
    def new_s(new_salary):
            curs.execute(f"update employee set salary = '{new_salary}' where id = {num} returning *")
            curs.execute("commit")
    def new_l(new_level):
            curs.execute(f"update employee set level = '{new_level}' where id = {num} returning *")
            curs.execute("commit")
    def new_t(new_title):
            curs.execute(f"update employee set title = '{new_title}' where id = {num} returning *")
            curs.execute("commit")
    def new_m(new_memo):
            curs.execute(f"update employee set memo = '{new_memo}' where id = {num} returning *")
            curs.execute("commit")
    print("输入id")
    num = input()
    print("输入部门编号")
    new_department_id =input()
    print("输入姓名")
    new_name = input("")
    print("输入性别")
    new_sex = input("")
    print("输入出生日期")
    new_birthdate = input("")
    print("输入家庭住址")
    new_address = input("")
    print("输入工作日期")
    new_work_date = input("")
    print("输入工资")
    new_salary = input("")
    print("输入级别")
    new_level = input("")
    print("输入职位")
    new_title = input("")
    print("备注5")
    new_memo = input("")
    change_id(num)
    new_d_id(new_department_id)
    new_n(new_name)
    new_x(new_sex)
    new_bd(new_birthdate)
    new_ad(new_address)
    new_wd(new_work_date)
    new_s(new_salary)
    new_l(new_level)
    new_t(new_title)
    new_m(new_memo)

    try:
        curs.execute(f"select * from employee where id={num}")
        info = curs.fetchall()
        print(" id     | department_id | name  | sex   | birthdate             | address       | work_date             | salary| level |  title        | memo")
        print("--------+---------------+-------+-------+-----------------------+---------------+-----------------------+-------+-------+---------------+-----")
        for n_e_info in info:
            for index in range(0,11):
                print(n_e_info[index],end='\t| ')
            print()
    except (Exception, psycopg2.DatabaseError) as error:
                print(error)












