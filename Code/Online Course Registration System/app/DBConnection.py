import pyodbc

class DBConnection:
    def __init__(self):
        self.connection_string = (
            "Driver={ODBC Driver 18 for SQL Server};"
            "Server=DESKTOP-A0HCLAR\\SQLEXPRESS;"
            "Database=OnlineCourse_db;"
            "TrustServerCertificate=yes;"
            "Trusted_Connection=yes;"
        )
        self.connection = None

    def connect(self):
        try:
            self.connection = pyodbc.connect(self.connection_string)
            print("Connection Successful!!!")
        except pyodbc.Error as e:
            print("Error occurred: ", e)
            self.connection = None

    def close(self):
        if self.connection:
            self.connection.close()
            print("Connection closed.")

    def get_connection(self):
        return self.connection



