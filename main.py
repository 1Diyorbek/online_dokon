import psycopg2 as db
import os
from dotenv import load_dotenv

load_dotenv()


class Database:
    @staticmethod
    def connect(query: str, query_type:str):
        database = db.connect(
            host=os.getenv("db_host"),
            database=os.getenv("db_name"),
            user=os.getenv("db_user"),
            password=os.getenv("db_password")
        )
        cursor = database.cursor()
        cursor.execute(query)
        data_type = ["insert", "create", "update", "delete"]
        if query_type in data_type:
            database.commit()
            if query_type == "insert":
                return "inserted into"
            return "Sucsesfully"
        else:
            return cursor.fetchall()