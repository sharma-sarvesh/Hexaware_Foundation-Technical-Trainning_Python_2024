
#* Database Connectivity
# Connection String
# server/host - localhost - server_name\SQLEXPRESS
# port - 1433
# database - sample
# user - HRB-LT590\Windows
# password - ''
# driver - {ODBC Driver 18 for SQL Server}
# TrustServerCertificate=yes;
# Trusted_Connection - yes;



#* import pyodbc
# connection_string = (
#     "Driver={ODBC Driver 18 for SQL Server};"
#     "Server=DESKTOP-A0HCLAR\\SQLEXPRESS;"
#     "Database=demo;"
#     "TrustServerCertificate=yes;"
#     "Trusted_Connection=yes;"
#     )

# try:
#     pyodbc.connect(connection_string)
#     print("Connection Successful!!!")
# except pyodbc.Error as e:
#     print("Error occured: ", e)

#* CRUD operations in DB using Python
import pyodbc
def create_db_connection():
    try:
        connection_string = (
            "Driver={ODBC Driver 18 for SQL Server};"
            "Server=DESKTOP-A0HCLAR\\SQLEXPRESS;"
            "Database=demo;"
            "TrustServerCertificate=yes;"
            "Trusted_Connection=yes;"
            )

        conn = pyodbc.connect(connection_string)
        # print(conn)
        return conn

    except Exception as e:
        print("Error while connecting to the DB: {}".format(e))


#* Read DB Data using python
def read_data(conn):
    cur = conn.cursor()
    select_sql = "SELECT * FROM Student"
    try:
        cur.execute(select_sql)
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Error while reading the data - {e}")

conn = create_db_connection()
#read_data(conn)


#* Write Data in DB using python
def insert_data(conn):
    cur = conn.cursor()
    insert_sql = "INSERT INTO Student VALUES ('Test1','Male',32,88,'7458745874','2024-12-27')"
    try:
        cur.execute(insert_sql)
        conn.commit()
    except Exception as e:
        print("Error while inserting the data - {}".format(e))
    else:
        print("Records inserted Successfully")
conn = create_db_connection()
# insert_data(conn)


#* Create Table in DB using python
def create_table(conn):
    cursor = conn.cursor()
    create_table_sql = '''
    CREATE TABLE Employees (
        ID INT PRIMARY KEY,
        Name VARCHAR(100),
        Age INT,
        Department VARCHAR(100)
    );
    '''
    try:
        cursor.execute(create_table_sql)
        conn.commit()
    except Exception as e:
        print("Error creating table: ", e)
    else:
        print("Table 'Employees' created successfully")

conn = create_db_connection()
#create_table(conn)


#* Delete data of DB using python
def delete_data(conn):
    cursor = conn.cursor()
    delete_sql = '''
    DELETE FROM Employees
    WHERE ID = ?;
    '''
    try:
        cursor.execute(delete_sql, (3,))
        conn.commit()
    except Exception as e:
        print("Error deleting data: ", e)
    else:
        print("Record deleted successfully")

conn = create_db_connection()
#delete_data(conn)


#* update data in DB using python
def update_data(conn):
    cursor = conn.cursor()
    update_sql = '''
    UPDATE Employees
    SET Age = ?
    WHERE ID = ?;
    '''
    try:
        cursor.execute(update_sql, (222222222, 1))
        conn.commit()
    except Exception as e:
        print("Error updating data:", e)
    else:
        print("Record updated successfully")

conn = create_db_connection()
update_data(conn)

#* delete table in DB using python
def delete_table(conn):
    cursor = conn.cursor()
    drop_sql = "DROP TABLE Employees;"

    try:
        cursor.execute(drop_sql)
        conn.commit()
    except Exception as e:
        print("Error deleting table: ", e)
    else:
        print("Table Deletion is successful")

conn = create_db_connection()
#delete_table(conn)

def read_data1(conn):
    cur = conn.cursor()
    select_sql = "SELECT * FROM Employees"
    try:
        cur.execute(select_sql)
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Error while reading the data - {e}")
conn = create_db_connection()
read_data1(conn)
