# insert data into the table in sql
# The Program Is Coded By Basanta chaudhary
import mysql.connector as mq
conn = mq.connect(host='localhost', user='root',
                  password='', database='student')
curob = conn.cursor()
#id_no = int(input('Enter ID No :'))
f_name = str(input('Fist_Name : '))
l_name = str(input('Last_Name : '))
sex = str(input('Gender : '))
age = int(input('Age : '))
sql = ('insert into basanta(first_name,last_name,gender,age) values ("{0}","{1}","{2}","{3}")'.format(
    f_name, l_name, sex, age))
if(conn.is_connected()):
    curob.execute(sql)
    conn.commit()
    print('Successfully Inserted Data !')
else:
    print('Unsucessfully Inserted Data !')
    
curob.close()
conn.close()
