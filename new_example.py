import psycopg2
import yaml


from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/v1/employees/<int:id>', methods=['GET'])
def get_employee(id):
    with open("postgresql/conf/manager.yaml", 'r') as f:
        db_config = yaml.load(f, Loader=yaml.FullLoader)
        postgres_config = db_config['database']['postgresql']
        host = postgres_config['host'];
        databaseName = postgres_config['databaseName']
        username = postgres_config['username']
        password = postgres_config['password']

        try:
            conn = psycopg2.connect(dbname=databaseName, user=username, host=host, password=password)
            with conn.cursor() as curs:
                    curs.execute("select * from employee where id = " + str(id))
                    pg_row = curs.fetchone()    
                    emp = {}
                    emp['id'] = pg_row[0]
                    emp['department_id'] = pg_row[1]
                    emp['name'] = pg_row[2]
                    return jsonify(emp)
        except:
            return jsonify("I am unable to connect to the database")
    return jsonify("error")

@app.route('/v1/employees', methods=['GET'])
def get_employees():
    employees =[]
    with open("postgresql/conf/manager.yaml", 'r') as f:
        db_config = yaml.load(f, Loader=yaml.FullLoader)
        postgres_config = db_config['database']['postgresql']
        host = postgres_config['host'];
        databaseName = postgres_config['databaseName']
        username = postgres_config['username']
        password = postgres_config['password']

        try:
            conn = psycopg2.connect(dbname=databaseName, user=username, host=host, password=password)
        except:
            print("I am unable to connect to the database")
        with conn.cursor() as curs:
                curs.execute("select * from employee")
                pg_rows = curs.fetchall()
                for pg_row in pg_rows:
                    emp = {}
                    emp['id'] = pg_row[0]
                    emp['department_id'] = pg_row[1]
                    emp['name'] = pg_row[2]
                    employees.append(emp)         
                return jsonify(employees)
                

if __name__ == '__main__':
    app.run(debug=True)


# create a connection using psycopg
# insert 100 records into employee table
# update a record in employee table by id 0
# delete a record from employee table by id 0
# query all data from employee table and print the contents to stdout