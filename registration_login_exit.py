import psycopg2
from typing import Any
def make_conn():
    conn = psycopg2.connect(
        database="uraaa",
        user="postgres",
        password="Nigga.01",
        host="localhost"
    )
    return conn
def destroy_conn(conn):
    conn.close()
class Registration:
    def append_users(self, username: str, password: str):
        conn = make_conn()
        curr = conn.cursor()
        query = f"INSERT INTO reg_log (username, password) VALUES ('{username}', '{password}')"
        curr.execute(query)
        conn.commit()   
        destroy_conn(conn)        
        print("Your login and password saved successfully!")
    
    def check_user(self, username: str, password: str):
        conn = make_conn()
        curr = conn.cursor()
        query = f"SELECT * FROM reg_log WHERE username = '{username}' AND password = '{password}'"
        curr.execute(query)
        result = curr.fetchone()
        destroy_conn(conn)  
        
        if result:
            print("User found.")
            return True
        else:
            print("Invalid username or password. Please try again.")
            return False
            