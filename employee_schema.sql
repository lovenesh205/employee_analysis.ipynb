CREATE DATABASE IF  NOT EXISTS  employee_db;
USE employee_db; 

CREATE TABLE employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department_id INT,
    salary DECIMAL(10,2),
    gender ENUM('male', 'female', 'other'),
    hire_date DATE
);

CREATE TABLE departments(
dep_id INT NOT NULL,
dept_name VARCHAR(100) NOT NULL,
manager_id INT NOT NULL
);

CREATE TABLE attendance(
emp_id INT NOT NULL,
date DATE,
status ENUM('Presnet','Absent')
);


CREATE TABLE performance(
emp_id int not null,
year DATE,
rating ENUM('5','4','3','2','1')
);









