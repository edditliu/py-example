CREATE TABLE department (
	id int4 primary key,
	name varchar(255) NULL,
	"function" varchar(255) NULL,
	manager varchar(255) NULL
);

--insert into department
INSERT INTO department (id,"name","function",manager) VALUES
	 (1,'r&d','reserch and development','Joseph Martin'),
	 (2,'sales','sale','Patricia Clark'),
	 (3,'test','test product','Margaret Brown'),
	 (4,'implementation','executive command','Laura Walker'),
	 (5,'finace','manage money','Cynthia Davis');
	 

CREATE table employee (
    id int4 primary key, 
    department_id int4,
    name varchar(255),
    sex varchar(2),
    birthdate timestamp without time zone,
    address varchar(255),
    work_date timestamp without time zone,
    salary int,
    level varchar(2),
    title varchar(24),
    memo text,
     CONSTRAINT fk_department_id
      FOREIGN KEY(department_id) 
	  REFERENCES department(id)
);

insert into employee (id, department_id, name, sex, birthdate, address, work_date, salary, level,title) VALUES
    (1,1, 'WangMing', '男', '1998-11-11', 'Beijing', '2023-01-01', 7272, 'P1', 'Developer');
insert into employee (id, department_id, name, sex, birthdate, address, work_date, salary, level,title) VALUES
    (2,2, 'LiMIng', '男', '1998-10-1', 'Nanjing', '2022-05-06',5320, 'P3', 'saler');
insert into employee (id, department_id, name, sex, birthdate, address, work_date, salary, level,title) VALUES
    (3,3, 'LiuQiang', '男', '1996-05-05', 'Shandong', '2012-05-04',52352,'P1', 'tester');
insert into employee (id, department_id, name, sex, birthdate, address, work_date, salary, level,title) VALUES
    (4,4, 'HuangYing', '女','1996-04-03', 'Jinan', '2021-08-06',5333, 'P4','performer' );
insert into employee (id, department_id, name, sex, birthdate, address, work_date, salary, level,title) VALUES
    (5,5, 'Jiafang', '女', '1999-06-08', 'Qingdao', '2020-05-09',7638, 'P2', 'accountant');
insert into employee (id, department_id, name, sex, birthdate, address, work_date, salary, level,title) VALUES
    (6,2, 'FangNan', '男', '1994-05-09', 'Neimenggu', '2019-04-08', 7554, 'P3', 'Senior Merchandiser');
insert into employee (id, department_id, name, sex, birthdate, address, work_date, salary, level,title) VALUES
    (7,3, 'Shanbing', '男', '1998-07-05', 'Huangming', '2014-05-02', 7888, 'P2', 'Software Tester');
insert into employee (id, department_id, name, sex, birthdate, address, work_date, salary, level,title) VALUES
    (8,1, 'JiaTanChun', '女', '1990-06-08', 'Huangshan', '2017-07-09', 9779, 'P2', 'Software Architec');
