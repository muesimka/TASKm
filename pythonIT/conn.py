import mysql.connector
#pip install mysql-connector-python
#1 создать подключение
connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="123456",
        database="academy"
    )
#2 создать курсор
cursor = connection.cursor()
#3 обьявить команду
cursor.execute("select  * from teachers")
#4 достаем данные
rows = cursor.fetchall()
for row in rows:
    print(row)
#5 закрываем соединения
cursor.close()