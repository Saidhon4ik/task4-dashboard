import os

import psycopg
from dotenv import load_dotenv


load_dotenv()

database_url = os.getenv("DATABASE_URL")

with psycopg.connect(database_url) as connection:
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM books")
        total_books = cursor.fetchone()[0]
        print(f"Books in the database: {total_books}")