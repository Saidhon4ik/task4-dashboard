import os

import psycopg
from dotenv import load_dotenv
from flask import Flask

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
    total = query("SELECT COUNT(*) FROM books")[0][0]
    return f"<h1>Books dashboard</h1><p>Books in database: {total}</p>"


if __name__ == "__main__":
    app.run(debug=True)