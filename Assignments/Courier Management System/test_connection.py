import pyodbc

try:
    conn = pyodbc.connect(
        "Driver={ODBC Driver 18 for SQL Server};"
        "Server=DESKTOP-A0HCLAR\\SQLEXPRESS;"
        "Database=CourierManagement_db;"
        "TrustServerCertificate=yes;"
        "Trusted_Connection=yes;"
    )
    print("Connection successful")
    conn.close()
except Exception as e:
    print("Error:", e)
