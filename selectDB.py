import sqlite3


with sqlite3.connect('employee.db') as conn:
    curs = conn.cursor()
    curs.execute("SELECT * FROM employee")
    rows = curs.fetchall()
    for item in rows:
        print(item[0],"  ",item[1],"  ",item[2])
