
# Digital Asset Management System

## Overview:
The Digital Asset Management System is a software application designed to manage and track assets, their maintenance, and allocation within an organization. The system provides functionalities for asset management, tracking maintenance records, allocating assets to employees, and making reservations.

=> This project is implemented using Python and MSSQL Server, following the Object-Oriented Programming (OOP) principles and a modular architecture.

## Key Components
#### Entity Layer: 
Contains classes that represent the database tables such as Asset, Employee, MaintenanceRecord AssetAllocation, and Reservation. These classes include attributes and getter/setter methods.

#### DAO Layer: 
The data access layer manages the interaction between the Python code and the MSSQL database. It includes the AssetManagementService interface and its implementation AssetManagementServiceImpl.

#### Exception Handling: 
Custom exceptions (AssetNotFoundException, AssetNotMaintainException) ensure meaningful error messages and prevent improper operations.

#### Utility: 
DBConnection.py manages the database connection, reading configurations from config.properties.

#### Main Application: 
The application logic in AssetManagementApp.py provides a menu-driven interface for users to interact with the system.

# Prerequisites
* Python 3.x
    - [Download Python](https://www.python.org/downloads/)
* MSSQL Server with the AssetManagement_db database
   - [Download SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)
* ODBC Driver 18 for SQL Server
* Required Python libraries: pyodbc, datetime, etc.


## Steps to Run the Digital Asset Management Application

1. **Clone the GitHub Repository**
   - Clone the repository to your local machine using the following command:
     ```bash
     git clone https://github.com/sharma-sarvesh/Hexaware_CaseStudy
     ```
   - Navigate to the project directory:
     ```bash
     cd your-repo-name
     ```

2. **Set Up the Database**
   - Make sure you have MSSQL Server installed and running.
   - Open SQL Server Management Studio (SSMS) or any SQL tool and connect to your database server.
   - Run the `AssetManagement_DB.sql` script found in the root folder of the project to create the required tables (`Assets`, `Employees`, `Asset_Allocations`, `Maintenance_Records`, `Reservations`, etc.):
     ```sql
     -- Example to run the script in SQL Server Management Studio
     -- Execute the following commands to create the database
     CREATE DATABASE AssetManagement_DB;
     USE AssetManagement_DB;
     -- Run the script content from the file `AssetManagement_DB.sql`
     ```

3. **Set Up Virtual Environment**
   - Create a virtual environment for Python dependencies:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - For **Windows**:
       ```bash
       venv\Scripts\activate
       ```
     - For **Mac/Linux**:
       ```bash
       source venv/bin/activate
       ```

4. **Install Required Dependencies**
   - With the virtual environment activated, install the necessary Python packages by running:
     ```bash
     pip install pyodbc
     ```

5. **Configure Database Connection**
   - Locate the `config.properties` file in the root folder and ensure the correct MSSQL database connection settings:
     ```properties
     [DatabaseConfig]
     driver = {ODBC Driver 18 for SQL Server}
     server = DESKTOP-A0HCLAR\SQLEXPRESS
     database = AssetManagement_DB
     trusted_connection = yes
     ```

6. **Run the Application**
   - Start the application by running the `AssetManagementApp.py` file:
     ```bash
     python app/AssetManagementApp.py
     ```
   - Follow the menu-driven interface to interact with the system (e.g., add assets, allocate assets, perform maintenance, reserve, or deallocate assets).

7. **Testing the Application**
   - The project includes some sample data in the SQL script for testing. You can interact with this data by using the options in the application’s menu.

8. **Deactivate the Virtual Environment (optional)**
   - After running the application, you can deactivate the virtual environment:
     ```bash
     deactivate
     ```

## Additional Notes
- If you encounter issues, check that your SQL Server is running, and ensure the database connection details in `config.properties` are correct.
- For further customization, update the `config.properties` file with your specific MSSQL Server settings.
