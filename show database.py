import mysql.connector as mq
conn=mq.connect(host='localhost',user='root',password='')
curobj=conn.cursor()
sql=str(input('Enter Commands : '))
if(conn.is_connected()):
    curobj.execute(sql)
    for x in curobj:
        print(x)
    print('Successfully !')
else:
    print('Unsuccessfully !')
conn.close()