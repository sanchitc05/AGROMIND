import sqlite3
import hashlib

def create_user_table():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS users(username TEXT PRIMARY KEY, password TEXT, question TEXT, answer TEXT)"
    )
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def add_user(username, password, question, answer):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (username, password, question, answer))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def login_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    data = c.fetchone()
    conn.close()
    return data

def get_user_question(username):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT question FROM users WHERE username=?", (username,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None

def verify_answer(username, answer):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT answer FROM users WHERE username=?", (username,))
    result = c.fetchone()
    conn.close()
    return result and result[0] == answer

def update_password(username, new_password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("UPDATE users SET password=? WHERE username=?", (new_password, username))
    conn.commit()
    conn.close()