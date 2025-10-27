from pathlib import Path
import sqlite3

DB = Path("./login.db")


def init_db():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)"
    )
    cur.execute(
        "INSERT OR IGNORE INTO users(username,password) VALUES(?,?)",
        ("demo", "P@ssw0rd"),
    )
    con.commit()
    con.close()


def get_user(username: str):
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE username=?", (username,))
    row = cur.fetchone()
    con.close()
    return dict(row) if row else None
