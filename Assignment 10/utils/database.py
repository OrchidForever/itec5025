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
        except psycopg2.Error as e:
            print(f"[Error]: Error connecting to PostgreSQL database: {e}")
            self.connection = None

    def add_media(self, title, format, owner, location):
        if self.connection is None:
            print("[Error]: No active database connection.")
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
            return True
        except psycopg2.Error as e:
            print(f"[Error]: Error adding media: {e}")
            return False

    def search_media_by_name(self, name):
        if self.connection is None:
            print("[Error]: No active database connection.")
            return []

        try:
            cursor = self.connection.cursor()
            search_query = sql.SQL("""
                SELECT * FROM media WHERE title ILIKE %s
            """)
            cursor.execute(search_query, (f"%{name}%",))
            results = cursor.fetchall()
            cursor.close()
            return results
        except psycopg2.Error as e:
            print(f"[Error]: Error searching media: {e}")
            return []

    def search_media_by_name_and_format(self, name, format):
        if self.connection is None:
            print("[Error]: No active database connection.")
            return []

        try:
            cursor = self.connection.cursor()
            search_query = sql.SQL("""
                SELECT * FROM media WHERE title ILIKE %s AND format ILIKE %s
            """)
            cursor.execute(search_query, (f"%{name}%", f"%{format}%"))
            results = cursor.fetchall()
            cursor.close()
            return results
        except psycopg2.Error as e:
            print(f"[Error]: Error searching media by name and format: {e}")
            return []

    def update_media_status(self, name, status):
        if self.connection is None:
            print("[Error]:No active database connection.")
            return False

        try:
            cursor = self.connection.cursor()
            update_query = sql.SQL("""
                UPDATE media SET status = %s WHERE title ILIKE %s
            """)
            cursor.execute(update_query, (status, f"%{name}%"))
            self.connection.commit()
            cursor.close()
            return True
        except psycopg2.Error as e:
            print(f"[Error]: Error updating media status: {e}")
            return False

    def update_media_status_by_name_and_format(self, name, format, status):
        if self.connection is None:
            print("[Error]: No active database connection.")
            return False

        try:
            cursor = self.connection.cursor()
            update_query = sql.SQL("""
                UPDATE media SET status = %s WHERE title ILIKE %s AND format ILIKE %s
            """)
            cursor.execute(update_query, (status, f"%{name}%", f"%{format}%"))
            self.connection.commit()
            cursor.close()
            return True
        except psycopg2.Error as e:
            print(f"[Error]: Error updating media status by name and format: {e}")
            return False

    def execute_query(self, query, params=None):
        if self.connection is None:
            print("[Error]: No active database connection.")
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
        except psycopg2.Error as e:
            print(f"[Error]: Error executing query: {e}")
            return None

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None
