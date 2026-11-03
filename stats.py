import os

import psycopg
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")


def query(sql, values=()):
    """Run one SQL query and return its rows."""
    with psycopg.connect(DATABASE_URL) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, values)
            return cursor.fetchall()


def books_in_year(year):
    """Return how many books were published in the given year."""
    rows = query("SELECT COUNT(*) FROM books WHERE year = %s", (year,))
    return rows[0][0]