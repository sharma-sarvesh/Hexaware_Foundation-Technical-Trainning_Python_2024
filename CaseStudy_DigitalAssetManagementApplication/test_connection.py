from util.DBConnection import DBConnection

# Test connection
conn = DBConnection.get_connection()
if conn:
    print("Connection successful")
else:
    print("Connection failed")
