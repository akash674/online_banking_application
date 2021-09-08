import pymysql


def get_mysql_connection():
    connection = None
    try:
        connection = pymysql.connect(host='localhost',
                                               database='online_banking',
                                               user='root',
                                               password='vishalR@2019')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except:
        print("Error while connecting to MySQL")
    return connection





