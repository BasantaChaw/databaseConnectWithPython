import mysql.connector as mq
conn = mq.connect(host='localhost', user='root', password='')
curob = conn.cursor()
data_name = str(input('Enter The Database Name : '))
sql = ('drop database '+data_name)
if(conn.is_connected()):
    curob.execute(sql)
    print('Successfully Deleted Database !')
else:
    print('Unsuccessfully Deleted Database !')
conn.close()
