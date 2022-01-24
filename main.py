
import sqlite3
from employee import Employee

conn = sqlite3.connect('employee.db')
# Creating connection object and also creating employee DB file 

c= conn.cursor()
#Create a cursor which allows us to excute some SQL statements 

# """ """ used for writing doc string. this is often used to write multiple lines of code withour any issues and 
#is often used in Python, herein we can put multiple lines of SQL code as well 

# Data types in Python "
# INTEGER - for interger values 
# REAL - for floating poitn decimals 
# TEXT - The value is a text string 
# BLOB - A Binary Large OBject (BLOB) is a collection of binary data stored as a single entity

#======= CREATE a TABLE using sqlite3==================================
# c.execute(""" CREATE TABLE employee( first text, last text, pay integer)""")

#================INSERTING THE DATA into the table created =============
# c.execute("INSERT INTO employee VALUES('Amit', 'Dhanray', 40000)")

emp1 = Employee('Hoang', 'Nguyen', 38000)
emp2 = Employee('Tien', 'Nguyen', 30000)
emp3 = Employee('Thanh', 'Vo', 23000)
# INSERTING THE DATA Method 1 
c.execute("INSERT INTO employee VALUES('{}', '{}', {})".format(emp1.first, emp1.fullname, emp1.pay))

# INSERTING THE DATA Method 2 
c.execute("INSERT INTO employee VALUES(?, ?, ?)", (emp2.first, emp2.fullname, emp2.pay))

# INSERTING THE DATA Method 3
c.execute("INSERT INTO employee VALUES(:f_name, :l_name, :var_sal)", {'f_name': emp3.first, 'l_name': emp3.last, 'var_sal': emp3.pay})


#====================SELECTING THE DATA====================
# c.execute("select * from employee where pay = :sal_var", {'sal_var': 23000})
print(c.fetchall())

conn.commit()
conn.close()