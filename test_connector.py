from tabloid.db.connector import DBConnector

conn = DBConnector("localhost", 5433, "postgres", "tabloid123", "postgres")
result = conn.connect()
print(f"Connected: {result}")
conn.disconnect