#!/usr/bin/python3
import pymysql


class Config:
    def __init__(self):
        pass

    __db = '';
    __cursor = ''

    def connection(self):
        print ("Connect to database...")
        # Open database connection
        db = pymysql.connect("localhost", "root", "tiffany", "jireh")
        self.__db = db

        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        self.__cursor = cursor

    def db(self):
        return self.__db

    def cursor(self):
        return self.__cursor


class Model:
    def __init__(self):
        pass

    @staticmethod
    def getAllUsers():
        # Prepare SQL query to INSERT a record into the database.
        sql = "SELECT id, username, nama_lengkap FROM users"
        try:
            config = Config()
            config.connection()
            db = config.db()
            cursor = config.cursor()
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            # disconnect from server
            db.close()

            return results
        except Exception as ex:
            print (ex)
