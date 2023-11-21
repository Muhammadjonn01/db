import psycopg2

conn = psycopg2.connect(
    database = "uraaa", user = "postgres", password = "Nigga.01", host = "localhost"
)
print(conn)
curr = conn.cursor()
def create_table():
    curr.execute("""
    CREATE TABLE usersss
    (
        id serial PRIMARY KEY,
        user_name varchar(25),
        user_password varchar(255)
    );                      
    """)
    rows = curr.fetchall()
    for row in rows:
       print(row)