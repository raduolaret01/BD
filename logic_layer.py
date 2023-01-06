
import mysql.connector


def get_catalog() -> list:
    result = list()
    try:
        connection = mysql.connector.connect(host='localhost',
                                             port='3307',
                                             database='tema_bd',
                                             user='root',
                                             password='ricardo44!')

        sql_query = "SELECT book_id, title, author FROM books"

        cursor = connection.cursor(buffered=True)
        cursor.execute(sql_query)
        for (book_id, title, author) in cursor:
            result.append((book_id, title, author))
        return result

    except mysql.connector.Error as error:
        print("MySQL Connector error: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def lend_book(cart, lend_date, return_date):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             port='3307',
                                             database='tema_bd',
                                             user='root',
                                             password='ricardo44!')

        cursor = connection.cursor(buffered=True)
        cursor.execute("start transaction")

        for (book_id) in cart:
            cursor.execute("select lend_date, return_date from book_lendings")
            for (lend_date_existing, return_date_existing) in cursor:
                if lend_date_existing < lend_date < return_date_existing or \
                        lend_date_existing < return_date < return_date_existing:
                    raise ValueError
            cursor.fetchall()
            sqlquery = "insert into book_lendings (book_id, user_id, lend_date, return_date) values ({}, 1, '{}', '{}')"\
                .format(book_id, lend_date, return_date)

            cursor.execute(sqlquery)

        cursor.execute("rollback")

    except mysql.connector.Error as error:
        if connection.is_connected():
            cursor.execute("rollback")

        print("MySQL Connector error: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def register_user(username, password):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             port='3307',
                                             database='tema_bd',
                                             user='root',
                                             password='ricardo44!')

        cursor = connection.cursor(buffered=True)
        cursor.execute("insert into users (username, pass) values ('{}', '{}')".format(username, password))

    except mysql.connector.Error as error:
        print("MySQL Connector error: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def login(username, password):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             port='3307',
                                             database='tema_bd',
                                             user='root',
                                             password='ricardo44!')

        cursor = connection.cursor(buffered=True)
        cursor.execute("select from users is_admin where username = '{}' and pass = '{}'".format(username, password))
        if cursor.rowcount() == 0:
            raise ValueError
        return cursor.fetchone()

    except mysql.connector.Error as error:
        print("MySQL Connector error: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")