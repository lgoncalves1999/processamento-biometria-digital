import pymysql.cursors

connection = pymysql.connect(host='127.0.0.1',
                         port=3306,
                         user='root',
                         password='',                             
                         db='none',
                         charset='utf8mb4',
                         autocommit=True,
                         cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
    query = 'SELECT * FROM sys.cadastro_teste;'
    cursor.execute(query)
connection.close()