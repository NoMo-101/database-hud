from tabloid.db.connector import DBConnector
from tabloid.db.inspector import SchemaInspector
from tabloid.engine.layout import LayoutEngine

# Test for Module 1: DBConnector; Filename: connector.py
# conn = DBConnector("localhost", 5433, "postgres", "tabloid123", "postgres")
# result = conn.connect()
# print(f"Connected: {result}")
# conn.disconnect()


# Test for Module 2: SchemaInspector; Filename: inspector.py
# conn = DBConnector("127.0.0.1", 5432, "tripuser", "trippassword123", "tripplanner")
# conn.connect()
# inspector = SchemaInspector(conn.connection)
# print("Tables: ", inspector.fetch_tables())
# print("Columns: ", inspector.fetch_columns())
# print("Foreign Keys: ", inspector.fetch_foreign_keys())
# conn.disconnect()

# Test for Module 3: LayoutEngine; Filename: layout.py
conn = DBConnector("127.0.0.1", 5432, "tripuser", "trippassword123", "tripplanner")
conn.connect()
inspector = SchemaInspector(conn.connection)

tables = inspector.fetch_tables()
foreign_keys = inspector.fetch_foreign_keys()

layout = LayoutEngine(tables, foreign_keys)
positions = layout.compute_layout()

print("Positions: ", positions)