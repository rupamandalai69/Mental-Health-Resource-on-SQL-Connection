import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mental_health_resources_db"
)

print("Database Connected Successfully")