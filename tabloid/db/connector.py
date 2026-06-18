import psycopg

class DBConnector:
    def __init__(self, host, port, user, password, dbname):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.dbname = dbname
        self.connection = None

    # Opens a connection to the Postgres database
    def connect(self):
        try:
            self.connection = psycopg.connect(
                host = self.host,
                port = self.port,
                user = self.user, 
                password = self.password,
                dbname = self.dbname
                )
            return True
        except psycopg.OperationalError as error:
            print(f"Connection error: {error}")
            return False
    # Closes the connection if one is open    
    def disconnect(self):
        if self.connection:
            self.connection.close()
        self.connection = None