import sqlite3
import subprocess
import hashlib
import os

# Hardcoded secret
SECRET_KEY = "mysecretkey123"

def get_user(user_id):
    conn = sqlite3.connect("users.db")
    # SQL Injection
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return conn.execute(query).fetchall()

def ping(host):
    # Command Injection
    return subprocess.check_output(f"ping -c 1 {host}", shell=True)

def hash_password(password):
    # Weak hashing
    return hashlib.md5(password.encode()).hexdigest()

def read_file(filename):
    # Path traversal potentiel
    with open(filename, "r") as f:
        return f.read()
