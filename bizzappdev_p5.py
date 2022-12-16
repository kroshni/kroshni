import sqlite3
conn=sqlite3.connect("bizzappdev_sqlite.py")

# Creating Table

conn.execute('''
    Create table employee(
        emp_id INT AUTO_INCREMENT PRIMARY KEY,
        emp_name VARCHAR(50),
        emp_email VARCHAR(50),
        emp_phone VARCHAR(50),
        emp_address VARCHAR(50),
        emp_gender VARCHAR(50)
    )
''')
conn.execute('''
    Create table department(
        dpt_id INT AUTO_INCREMENT PRIMARY KEY,
        emp_id INT NOT NULL,
        dpt_name VARCHAR(50),
        FOREIGN KEY (emp_id) REFERENCES employee(emp_id)
    )
''')
conn.execute('''
    Create table project(
        project_id INT AUTO_INCREMENT PRIMARY KEY,
        project_name VARCHAR(50),
        emp_id INT NOT NULL,
        from_date DATE,
        end_date DATE,
        FOREIGN KEY (emp_id) REFERENCES employee(emp_id)
    )
''')

# Inserting Data

conn.execute('''
    INSERT INTO employee (emp_id,emp_name,emp_email,emp_phone,emp_address,emp_gender) VALUES
    (1,'Willson Patrick','willson@gmail.com','9999999999','New York (US)','Male'),
    (2,'Richard','richard@gmail.com','9999999991','New York (US)','Male'),
    (3,'Jasmine','jasmine@gmail.com','9999999992','New York (US)','Female'),
    (4,'Rossy','rossy@gmail.com','9999999993','New York (US)','Female'),
    (5,'Aleena','aleena@gmail.com','9999999994','New York (US)','Female')
''');
conn.commit()
conn.execute('''
    INSERT INTO department (emp_id,dpt_name) VALUES 
    (1,'PHP Developer'), 
    (2,'Frontend Developer'), 
    (3,'Magento Developer'), 
    (4,'Python Developer'), 
    (5,'Backend Developer')
''');
conn.commit()
conn.execute('''
    INSERT INTO project (project_name,emp_id,from_date,end_date) VALUES 
    ('Tipster',1,'2017-06-20','2018-07-20'),  
    ('PSCS',2,'2015-06-20','2017-07-20'),  
    ('Trueopinion',2,'2014-06-20','2015-07-20'),  
    ('Wecharge',1,'2014-02-20','2015-01-20'),  
    ('Cuffs N Lashes',1,'2016-06-20','2019-07-20')
''');
conn.commit()

conn.close()