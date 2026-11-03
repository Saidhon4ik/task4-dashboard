import os

import psycopg
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()
app = Flask(__name__)
DATABASE_URL = os.getenv("DATABASE_URL")


def query(sql, values=()):
    """Run one SQL query and return its rows."""
    with psycopg.connect(DATABASE_URL) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, values)
            return cursor.fetchall()


@app.get("/")
def dashboard():
    genre = request.args.get("genre", "")
    search = request.args.get("search", "")

    filters = []
    values = []
    if genre:
        filters.append("genre = %s")
        values.append(genre)
    if search:
        filters.append("(title ILIKE %s OR author ILIKE %s)")
        values.extend([f"%{search}%", f"%{search}%"])

    where = " WHERE " + " AND ".join(filters) if filters else ""

    total = query(f"SELECT COUNT(*) FROM books{where}", values)[0][0]
    genres = query("SELECT DISTINCT genre FROM books WHERE genre IS NOT NULL ORDER BY genre")
    counts = query(
        f"SELECT genre, COUNT(*) FROM books{where} GROUP BY genre ORDER BY COUNT(*) DESC LIMIT 10",
        values,
    )
    books = query(
        f"SELECT title, author, genre, year FROM books{where} ORDER BY title LIMIT 25",
        values,
    )

    return render_template(
        "index.html", total=total, genres=genres, counts=counts, books=books,
        selected_genre=genre, search=search,
    )


if __name__ == "__main__":
    app.run(debug=True)