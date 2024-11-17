# app/CourierManagementSystem.py

import sys
import os

# Adding the project root directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'S:\GIT\Hexaware_Assignments\Courier Management System')))

from dao.UserDAOImpl import UserDAOImpl
from dao.EmployeeDAOImpl import EmployeeDAOImpl
from dao.PaymentDAOImpl import PaymentDAOImpl
from dao.CourierServicesDAOImpl import CourierServicesDAOImpl
from dao.CourierDAOImpl import CourierDAOImpl
from entity.User import User
from entity.Employee import Employee
from entity.Payment import Payment
from entity.Courier import Courier
from entity.CourierServices import CourierService

def main():
    user_dao = UserDAOImpl()
    employee_dao = EmployeeDAOImpl()
    payment_dao = PaymentDAOImpl()
    courier_service_dao = CourierServicesDAOImpl()
    courier_dao = CourierDAOImpl()

    while True:
        print("\n **** Courier Management System **** ")
        print(" 1. Create User")
        print(" 2. Delete User")
        print(" 3. Fetch User Details")
        print(" 4. Create Employee")
        print(" 5. Delete Employee")
        print(" 6. Fetch All Employees")
        print(" 7. Fetch Employee by ID")
        print(" 8. Insert New Courier")
        print(" 9. Update Courier Status")
        print("10. Get All Couriers")
        print("11. Create Courier Service")
        print("12. Update Courier Service")
        print("13. Delete Courier Service")
        print("14. Fetch Courier Service Details")
        print("15. List All Courier Services")
        print("16. Read Payment")
        print(" 0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            user_id = input("Enter User ID: ")
            name = input("Enter User Name: ")
            email = input("Enter Email: ")
            password = input("Enter Password: ")
            contact_number = input("Enter Contact Number: ")
            address = input("Enter Address: ")
            user = User(user_id, name, email, password, contact_number, address)
            user_dao.create_user(user)
            print("User created successfully!")

        elif choice == "2":
            user_id = input("Enter User ID to delete: ")
            user_dao.delete_user(user_id)
            print("User deleted successfully!")

        elif choice == "3":
            user_id = input("Enter User ID to fetch details: ")
            user = user_dao.get_user_by_id(user_id)
            if user:
                print(f"User Details: ID: {user.get_UserID()}, Name: {user.get_Name()}, Email: {user.get_Email()}, Address: {user.get_Address()}")
            else:
                print("User not found!")

        elif choice == "4":
            employee_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            email = input("Enter Email: ")
            contact_number = input("Enter Contact Number: ")
            role = input("Enter Role: ")
            salary = float(input("Enter Salary: "))
            employee = Employee(employee_id, name, email, contact_number, role, salary)
            employee_dao.create_employee(employee)
            print("Employee created successfully!")

        elif choice == "5":
            employee_id = input("Enter Employee ID to delete: ")
            
            # Convert employee_id to int (make sure to handle possible conversion errors)
            try:
                employee_id = int(employee_id)
            except ValueError:
                print("Invalid Employee ID. Please enter a numeric value.")
                continue  # or break, depending on your flow

            # Call the delete_employee method
            try:
                employee_dao.delete_employee(employee_id)
                print("Employee deleted successfully!")
            except Exception as e:
                print(f"An error occurred while deleting the employee: {e}")

        elif choice == "6":
            employees = employee_dao.get_all_employees()
            for emp in employees:
                print(f"Employee ID: {emp.get_EmployeeID()}, Name: {emp.get_Name()}, Role: {emp.get_Role()}")

        elif choice == "7":
            employee_id = input("Enter Employee ID to fetch: ")
            try:
                employee = employee_dao.get_employee_by_id(int(employee_id))  # Ensure employee_id is an integer
                if employee:
                    print(f"Employee Details:\n"
                        f"ID: {employee.get_EmployeeID()}\n"
                        f"Name: {employee.get_Name()}\n"
                        f"Email: {employee.get_Email()}\n"
                        f"Contact Number: {employee.get_ContactNumber()}\n"
                        f"Role: {employee.get_Role()}\n"
                        f"Salary: {employee.get_Salary()}")
                else:
                    print("Employee not found!")
            except InvalidEmployeeIdException as e:
                print(e)
            except ValueError:
                print("Please enter a valid integer for Employee ID.")
            except Exception as ex:
                print(f"An unexpected error occurred: {ex}")

        elif choice == "8":
            courier_id = input("Enter Courier ID: ")
            sender_name = input("Enter Sender Name (UserID): ")
            sender_address = input("Enter Sender Address: ")
            receiver_name = input("Enter Receiver Name (UserID): ")
            receiver_address = input("Enter Receiver Address: ")
            weight = float(input("Enter Weight: "))
            status = input("Enter Status: ")
            tracking_number = input("Enter Tracking Number: ")
            delivery_date = input("Enter Delivery Date (YYYY-MM-DD): ")
            courier = Courier(courier_id, sender_name, sender_address, receiver_name,
                                receiver_address, weight, status, tracking_number,
                                delivery_date)
            courier_dao.create_courier(courier)
            print("Courier order created successfully!")

        elif choice == "9":
            courier_id = input("Enter Courier ID to update status: ")
            new_status = input("Enter New Status: ")
            courier = courier_dao.get_courier_by_id(courier_id)
            if courier:
                courier.set_Status(new_status)
                courier_dao.update_courier(courier)
                print("Courier status updated successfully!")
            else:
                print("Courier not found!")

        elif choice == "10": 
            couriers = courier_dao.get_all_couriers()  
            if couriers:  
                print("All Couriers:")
                for courier in couriers:  
                    print(f"ID: {courier.get_CourierID()}, Sender: {courier.get_SenderName()}, Receiver: {courier.get_ReceiverName()}, Status: {courier.get_Status()}")
            else:
                print("No couriers found.")

        elif choice == "11":
            service_id = input("Enter Service ID: ")
            service_name = input("Enter Service Name: ")
            cost = float(input("Enter Cost: "))
            courier_service = CourierService(service_id, service_name, cost)
            courier_service_dao.create_courier_service(courier_service)
            print("Courier service created successfully!")

        elif choice == "12":
            service_id = input("Enter Service ID to update: ")
            courier_service = courier_service_dao.get_courier_service_by_id(service_id)
            if courier_service:
                service_name = input("Enter New Service Name (Leave blank for no change): ")
                if service_name:
                    courier_service.set_serviceName(service_name)
                cost = input("Enter New Cost (Leave blank for no change): ")
                if cost:
                    courier_service.set_Cost(float(cost))
                courier_service_dao.update_courier_service(courier_service)
                print("Courier service updated successfully!")
            else:
                print("Courier service not found!")

        elif choice == "13":
            service_id = input("Enter Service ID to delete: ")
            courier_service_dao.delete_courier_service(service_id)
            print("Courier service deleted successfully!")

        elif choice == "14":
            service_id = input("Enter Service ID to fetch details: ")
            courier_service = courier_service_dao.get_courier_service_by_id(service_id)
            if courier_service:
                print(f"Courier Service Details: ID: {courier_service.get_ServiceID()}, Name: {courier_service.get_ServiceName()}, Cost: {courier_service.get_Cost()}")
            else:
                print("Courier service not found!")

        elif choice == "15":
            services = courier_service_dao.get_all_courier_services()
            for service in services:
                print(f"Service ID: {service.get_ServiceID()}, Name: {service.get_ServiceName()}, Cost: {service.get_Cost()}")

        elif choice == "16":
            payment_id = input("Enter Payment ID to read: ")
            payment = payment_dao.get_payment_by_id(payment_id)
            if payment:
                print(f"Payment Details: ID: {payment.get_PaymentID()}, Amount: {payment.get_Amount()}, Date: {payment.get_PaymentDate()}")
            else:
                print("Payment not found!")

        elif choice == "0":
            print("Exiting Courier Management System...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
