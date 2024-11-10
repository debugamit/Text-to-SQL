#over here we are try to create a database with the python with help of sqlite 

import sqlite3 #sqlite3 is a database engine with base of python 

#connect sqlite 
conn=sqlite3.connect("student.db")

# create cursor to read and write the data (create object to insert record, retrive table and create table )
cur =  conn.cursor()

## create table 
table_info = """  
create table STUDENT (NAME char(25), CLASS varchar(25), SECTION varchar(25), MARKS int)
 """

cur.execute(table_info)

#insert some more records

cur.execute(''' Insert into STUDENT values ('Amit', ' Datascience', 'A', '90')''')
cur.execute(''' Insert into STUDENT values ('Raja', ' Science', 'C', '50')''')
cur.execute(''' Insert into STUDENT values ('Chuddu', ' Datascience', 'A', '100')''')
cur.execute(''' Insert into STUDENT values ('Dadiyal', ' Sports', 'B', '75')''')
cur.execute(''' Insert into STUDENT values ('Phunti', ' Datascience', 'B', '80')''')
cur.execute(''' Insert into STUDENT values ('Chenu', ' Datascience', 'C', '70')''')
cur.execute(''' Insert into STUDENT values ('Amit', ' Science', 'B', '85')''')


#Display all the record 
print(" The inserted records are  ")


data = cur.execute('''Select * from STUDENT''')

#here we are going to read the data from each row 
for row in data:
    print(row)



# we have to close the connection 
conn.commit()
conn.close()



