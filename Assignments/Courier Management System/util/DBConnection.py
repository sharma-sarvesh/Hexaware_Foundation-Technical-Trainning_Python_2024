import pyodbc

class DBConnection:
    connection = None

    @staticmethod
    def get_connection():
        if DBConnection.connection is None:
            try:
                # Define the connection string
                connection_string = (
                    "Driver={ODBC Driver 18 for SQL Server};"
                    "Server=DESKTOP-A0HCLAR\\SQLEXPRESS;"
                    "Database=CourierManagement_db;"  
                    "TrustServerCertificate=yes;"
                    "Trusted_Connection=yes;"
                )
                
                # Establish the database connection
                DBConnection.connection = pyodbc.connect(connection_string)
            except Exception as e:
                raise Exception(f"Error while establishing the database connection: {e}")
        return DBConnection.connection

    @staticmethod
    def close_connection():
        """Close the database connection if it exists."""
        if DBConnection.connection is not None:
            DBConnection.connection.close()
            DBConnection.connection = None
