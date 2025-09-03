import psycopg2
from psycopg2 import sql
import random
import string

class PostgreSQLDatabase:
    def __init__(self, dbname="postgres", user="postgres", password="password", host="localhost", port="5432"):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        try:
            # Establish the connection
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print("Connection to PostgreSQL database established.")
        except psycopg2.Error as e:
            print(f"Error connecting to PostgreSQL database: {e}")
            self.connection = None

    def add_media(self, title, format, owner, location):
        if self.connection is None:
            print("No active database connection.")
            return False

        try:
            cursor = self.connection.cursor()
            insert_query = sql.SQL("""
                INSERT INTO media (title, format, owner, location, status)
                VALUES (%s, %s, %s, %s, %s)
            """)
            cursor.execute(insert_query, (title, format, owner, location, "Available"))
            self.connection.commit()
            cursor.close()
            print(f"Media '{title}' added successfully.")
            return True
        except psycopg2.Error as e:
            print(f"Error adding media: {e}")
            return False

    def execute_query(self, query, params=None):
        if self.connection is None:
            print("No active database connection.")
            return None

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            if query.strip().lower().startswith("select"):
                result = cursor.fetchall()
                cursor.close()
                return result
            else:
                self.connection.commit()
                cursor.close()
                print("Query executed successfully.")
        except psycopg2.Error as e:
            print(f"Error executing query: {e}")
            return None

    def close(self):
        if self.connection:
            self.connection.close()
            print("Connection to PostgreSQL database closed.")
            self.connection = None
