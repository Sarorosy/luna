import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="sarorosy",
    database="ai"
)
print("Database connected successfully!")
