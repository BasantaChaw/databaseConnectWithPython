# create a table 'Student' in database using mysql in python
# The Program Is Coded By Basanta chaudhary
import mysql.connector as mq
conn = mq.connect(host='localhost', user='root',
                  password='', database='student')
curob = conn.cursor()
#table_name = str(input('Enter The Table Name : '))
sql = ('''
         create table basanta(
             id int auto_increment primary key,
             first_name varchar(20) not null,
             last_name varchar(20) not null,
             gender varchar(1) not null,
             age int not null
         )
      ''')
if(conn.is_connected()):
    curob.execute(sql)
    conn.commit()
    print('Successfully created table !')

else:

    print('Unsuccessfully created table !')
curob.close()
conn.close()
