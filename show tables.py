# show database table names in python
# The Program Is Coded By Basanta chaudhary
import mysql.connector as mq
conn = mq.connect(host='localhost', user='root', password='', database='mysql')
curob = conn.cursor()
if (conn.is_connected()):
    curob.execute('show tables')
    for x in curob:
        print(x)
    print('Successfully Show Tables !')
else:
    print('Unsuccesfully !')

curob.close()
conn.close()
