import pymysql
from config import host, user, password, db_name



try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("успешное подключение...")
    

    try:
        cursor = connection.cursor()

     
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `news`"
            cursor.execute(select_all_rows)
            # cursor.execute("SELECT * FROM `users`")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            

    finally:
        connection.close()

except Exception as ex:
    print("ошибка подключения...")
    print(ex)


 
 
