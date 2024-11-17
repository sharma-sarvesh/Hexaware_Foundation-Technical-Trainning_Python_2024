# util\DBConnection.py

import os
import configparser
import pyodbc

class DBConnection:
    connection = None

    @staticmethod
    def get_connection():
        if DBConnection.connection is None:
            config = configparser.ConfigParser()

            # Use the correct path with raw string literal
            config_path = r'S:\GIT\Hexaware_CaseStudy\app\config.properties'
            print(f"Reading config from: {config_path}")
            
            # Check if the file exists
            if not os.path.exists(config_path):
                print("config.properties file not found!")
                return None
            
            config.read(config_path)
            print("Config Sections: ", config.sections())  # <-- Debugging the sections
            
            try:
                driver = config.get('DEFAULT', 'driver')
                print(f"Driver: {driver}")
                
                server = config.get('DEFAULT', 'server')
                database = config.get('DEFAULT', 'database')
                trust_server_cert = config.get('DEFAULT', 'trustServerCertificate')
                trusted_connection = config.get('DEFAULT', 'trustedConnection')

                connection_string = (
                    f"Driver={{{driver}}};"
                    f"Server={server};"
                    f"Database={database};"
                    f"TrustServerCertificate={trust_server_cert};"
                    f"Trusted_Connection={trusted_connection};"
                )

                DBConnection.connection = pyodbc.connect(connection_string)
                print("Database connection established successfully.")
            except Exception as e:
                print(f"Error while connecting to the database: {e}")
        return DBConnection.connection

    @staticmethod
    def close_connection():
        if DBConnection.connection is not None:
            try:
                DBConnection.connection.close()
                print("Database connection closed successfully.")
            except Exception as e:
                print(f"Error while closing the database connection: {e}")
            finally:
                DBConnection.connection = None
