# util/DBConnection.py
import pyodbc

class DBConnection:
    connection = None

    @staticmethod
    def getConnection():
        if DBConnection.connection is None:
            try:
                # Define the connection string
                connection_string = (
                    "Driver={ODBC Driver 18 for SQL Server};"
                    "Server=DESKTOP-A0HCLAR\\SQLEXPRESS;"
                    "Database=HospitalManagement_DB;"
                    "TrustServerCertificate=yes;"
                    "Trusted_Connection=yes;"
                )
                
                # Establish the database connection
                DBConnection.connection = pyodbc.connect(connection_string)
            except Exception as e:
                print(f"Error while establishing the database connection: {e}")
                DBConnection.connection = None
        return DBConnection.connection
