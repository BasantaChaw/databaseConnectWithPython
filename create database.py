import mysql.connector as mq

conn=mq.connect(host='localhost',user='root',password='')
curobj=conn.cursor()
if (conn.is_connected()):
    sql='create database Student'
    curobj.execute(sql)
    print('Successfully created database !')
else:
    print('Unccessfully created Databse !')
conn.close()
