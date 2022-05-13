import mysql.connector as mq
conn = mq.connect(host='localhost', user='root', password='')
if(conn.is_connected):
    print('Successfully connection !')
else:
    print('UnSuccessfully connection !')
