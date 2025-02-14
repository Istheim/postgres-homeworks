-- SQL-команды для создания таблиц
CREATE TABLE customers (
  customer_id VARCHAR(10) PRIMARY KEY,
  company_name VARCHAR(100),
  contact_name VARCHAR(100)
);

CREATE TABLE employees (
  employee_id SERIAL PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  title VARCHAR(100),
  birth_date DATE,
  notes TEXT
);

CREATE TABLE orders (
  order_id SERIAL PRIMARY KEY,
  customer_id VARCHAR(10),
  employee_id INTEGER,
  order_date DATE,
  ship_city VARCHAR(100),
  FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
  FOREIGN KEY (employee_id) REFERENCES employees (employee_id)
);
