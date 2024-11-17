# DEMO
#* 1. order management system
# Build a simple order management system for an e-commerce platform. The system must handle the following tasks:
# Customer Details: Accept basic customer details like name, address, and phone number.
# Product Catalog: Maintain a list of products available for sale, where each product has a name, price, and stock quantity.
# Place Order: Customers should be able to place an order by providing the product names, quantity, and any optional information such as a promo code or delivery preference.
# Invoice Generation: Once an order is placed, generate an invoice that summarizes the total price, including any additional costs (such as taxes or shipping fees).
# Order Tracking: Store and track the placed orders using a dictionary, allowing you to print an order history at any time.

# Requirements and Hints:
# Use dictionaries to store customer details, product catalog, and orders.
# Use lists to store multiple products in the catalog and allow customers to order multiple items.
# Use *args to handle additional costs (e.g., taxes, shipping fees) while generating the invoice.
# Use **kwargs to handle additional information (e.g., promo codes, delivery preferences) while placing an order.
# Use loops and conditional statements to calculate the total price and ensure sufficient stock before placing the order.
# Use arbitrary argument lists and keyword arguments to manage flexibility in the order and invoice creation process.


# def Customer_Details():
#     print("Customer Details")
# def Product_Catalog():
#     print("Product Catalog")
# def Place_Order():
#     print("Place Order")
# def Invoice_Generation():
#     print("Invoice Generation")
# def Order_Tracking():
#     print("Order Tracking")

# def Order_Management_System():
#     while True:
#         print("\n1. Customer Details \n2. Product Catalog \n3. Place Order \n4. Order Tracking \n5. Exit")
#         choice = int(input("Enter your choice: \n"))

#         if choice == 1:
#             Customer_Details()
#         elif choice == 2:
#             Product_Catalog()
#         elif choice == 3:
#             Place_Order()
#         elif choice == 4:
#             Order_Tracking()
#         elif choice == 5:
#             print("End of Order Management Application")
#             break
#         else:
#             print("Enter Valid Choice")

# Order_Management_System()




#* 2. Employee Management System
# Scenario: Employee Management System
# Create an employee management system that can perform the following operations:
# Add employees with their details (name, role, salary).
# Calculate and display the salary of employees based on performance.
# List all employees.
# Find an employee by name.
# Update an employee's performance and recalculate the bonus.
# Use object-oriented programming to represent employees, roles, and performance. Use functions and modules to separate concerns.
# Requirements:
# Use statements, loops, and conditions to control the flow.
# Define functions for code modularity.
# Utilize OOP to represent employees.
# Break the code into modules.


#* 3. Hotel Booking System
# A simple system to handle room bookings for a hotel. It manages room availability, new bookings, and cancellations.
# Features:
# Room Management: Keep track of available rooms.
# Booking Management: Add new bookings, check availability, and cancel bookings.
# Room Pricing: Different rooms have different prices, which can vary based on the type (Single, Double, Suite).
# Search: Search for available rooms by date.
# Components:
# Classes: Room, Booking, Hotel.
# Methods:
# add_booking: Book a room for a given date.
# cancel_booking: Cancel a booking.
# check_availability: Check if a room is available on a specific date.
# get_booking_info: Get details about a booking.




#* Online Food Ordering System:
# Problem Statement: You need to design an Online Food Ordering System where customers can order food items, apply discount coupons, and pay for their orders. The system should handle the following:
'''
Manage a list of available food items.
Allow users to apply discount coupons.
Calculate the total bill after applying discounts.
Handle invalid coupon codes, unavailable items, and out-of-stock items.
Implement exception handling to manage:
    Invalid food item selection.
    Invalid or expired coupon codes.
    Out-of-stock items.
    Insufficient balance in payment.
Use polymorphism to allow different payment methods (credit card, debit card, wallet).
Use file handling to log order details.
''' 
#* Hints:
# Use classes to represent food items, coupons, and orders.
# Use inheritance to represent different payment methods (credit card, wallet).
# Use composition to link an order with food items and coupons.
# Implement exception handling for invalid selections and payments.
# Use file handling to log order details after successful payment.

import pyodbc
print(pyodbc.drivers())





#* Online Course Registration System
# Problem Statement:Develop an Online Course Registration System where:
'''
# Students can register for multiple courses, and each course has a unique Course ID, Course Name, and Instructor.
# Store student and course information in MSSQL tables.
# Allow students to register for courses, update their course list, or deregister from courses.
# Create a transaction log in a text file to keep track of all registration changes (add, update, delete).
# Use exception handling for scenarios like over-enrollment (more than 5 courses per student) or registering for a non-existent course.
# Handle OOP concepts to model relationships between Students, Courses, and Instructors.
'''
#* Tasks:
'''
# Create MSSQL tables to handle course registration and student data.
# Implement CRUD operations for course registration.
# Log registration details in a text file.
# Handle exceptions for over-enrollment and invalid course selection.
'''
#* Hints:
'''
# Create tables for Students, Courses, and Enrollments.
# Use file handling to log every course registration or modification.
# Apply try-except-else-finally blocks to handle errors during the registration process.
# Implement custom exceptions for exceeding course limits or invalid course selection.
'''
#* General Considerations :
# Focus on clean code practices, including appropriate naming conventions, modularity, and code reusability.
# Ensure proper use of exception handling and logging to manage unexpected scenarios.
# Solutions should handle edge cases such as invalid inputs, database connection issues, and logical errors in business rules.




