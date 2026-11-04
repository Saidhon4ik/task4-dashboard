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


def books_in_genre(genre):
    """Return how many books have the given genre, ignoring capital letters."""
    rows = query("SELECT COUNT(*) FROM books WHERE genre ILIKE %s", (genre,))
    return rows[0][0]


def average_price_in_year(year):
    """Return the average price in USD for books of the given year.

    Euro prices are converted at 1 EUR = 1.2 USD.
    Returns None if there are no books that year.
    """
    rows = query(
        "SELECT ROUND(AVG(CASE WHEN currency = '$' THEN price ELSE price * 1.2 END), 2) "
        "FROM books WHERE year = %s",
        (year,),
    )
    value = rows[0][0]
    return float(value) if value is not None else None