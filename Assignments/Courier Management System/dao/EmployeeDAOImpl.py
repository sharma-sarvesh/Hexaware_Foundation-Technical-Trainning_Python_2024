from dao.EmployeeDAO import EmployeeDAO
from util.DBConnection import DBConnection
from entity.Employee import Employee
from myexceptions.InvalidEmployeeIdException import InvalidEmployeeIdException
import pyodbc

class EmployeeDAOImpl(EmployeeDAO):
    
    def create_employee(self, employee: Employee) -> None:
        conn = DBConnection.get_connection()
        cursor = conn.cursor()
        query = '''INSERT INTO Employee (EmployeeID, Name, Email, ContactNumber, Role, Salary) 
                    VALUES (?, ?, ?, ?, ?, ?)'''
        values = (employee.get_EmployeeID(), employee.get_Name(), employee.get_Email(),
                    employee.get_ContactNumber(), employee.get_Role(), employee.get_Salary())
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()

    def get_employee_by_id(self, employee_id: int) -> Employee:
        conn = DBConnection.get_connection()
        cursor = conn.cursor()
        query = "SELECT EmployeeID, Name, Email, ContactNumber, Role, Salary FROM Employee WHERE EmployeeID = ?"
        cursor.execute(query, (employee_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return Employee(*row)  # Ensure it matches the columns: EmployeeID, Name, Email, ContactNumber, Role, Salary
        else:
            raise InvalidEmployeeIdException(f"Employee with ID {employee_id} does not exist.")
    
    def delete_employee(self, employee_id: int) -> None:
        try:
            with DBConnection.get_connection() as conn:
                with conn.cursor() as cursor:
                    query = "DELETE FROM Employee WHERE EmployeeID = ?"
                    cursor.execute(query, (employee_id,))
                    conn.commit()
                    print("Employee deleted successfully.")
        except pyodbc.Error as e:
            print(f"Database error occurred: {e}")
        except Exception as ex:
            print(f"An unexpected error occurred: {ex}")

    def get_all_employees(self) -> list:
        conn = DBConnection.get_connection()
        cursor = conn.cursor()
        query = "SELECT EmployeeID, Name, Email, ContactNumber, Role, Salary FROM Employee"
        cursor.execute(query)
        rows = cursor.fetchall()
        # cursor.close()
        # conn.close()
        return [Employee(*row) for row in rows]  # Ensure the number of fields matches the Employee class

    def update_employee(self, employee) -> None:
        try:
            with DBConnection.get_connection() as conn:
                with conn.cursor() as cursor:
                    # Fetch existing employee details
                    query = "SELECT EmployeeID, Name, Email, ContactNumber, Role, Salary FROM Employee WHERE EmployeeID = ?"
                    cursor.execute(query, (employee.get_EmployeeID(),))
                    existing_employee = cursor.fetchone()

                    if not existing_employee:
                        raise InvalidEmployeeIdException(f"Employee with ID {employee.get_EmployeeID()} does not exist.")

                    # Retain existing details if no new data is provided
                    name = employee.get_Name() if employee.get_Name() else existing_employee[1]
                    email = employee.get_Email() if employee.get_Email() else existing_employee[2]
                    contact_number = employee.get_ContactNumber() if employee.get_ContactNumber() else existing_employee[3]
                    role = employee.get_Role() if employee.get_Role() else existing_employee[4]
                    salary = employee.get_Salary() if employee.get_Salary() is not None else existing_employee[5]

                    # Update query
                    update_query = '''UPDATE Employee 
                                        SET Name = ?, Email = ?, ContactNumber = ?, Role = ?, Salary = ? 
                                        WHERE EmployeeID = ?'''
                    cursor.execute(update_query, (name, email, contact_number, role, salary, employee.get_EmployeeID()))
                    
                    # Commit the transaction
                    conn.commit()
                    print("Employee updated successfully.")
                    
        except pyodbc.Error as e:
            print(f"Database error occurred: {e}")
            # Optionally, you can raise the exception again if needed
            # raise
        except Exception as ex:
            print(f"An unexpected error occurred: {ex}")

        except pyodbc.ProgrammingError as e:
            print(f"Database error occurred: {e}")
            raise

        finally:
            # Ensure that the cursor and connection are closed, but only if they are defined
            if cursor:
                cursor.close()
            if conn:
                conn.close()
