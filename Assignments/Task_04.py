import re
import random
import string

def parcel_tracking():
    tracking_data = {
        "123": "In Transit",
        "456": "Out for Delivery",
        "789": "Delivered"
    }
    
    tracking_number = input("Enter your tracking number: ")
    status = tracking_data.get(tracking_number)

    if status:
        print(f"Tracking Number: {tracking_number}, Status: {status}")
        messages = {
            "In Transit": "Parcel is in transit.",
            "Out for Delivery": "Parcel is out for delivery.",
            "Delivered": "Parcel has been delivered."
        }
        print(messages[status])
    else:
        print("Tracking number not found.")

def validate_customer_data(data, detail):
    if detail == "name":
        if data.isalpha() and data.istitle():
            print("Name is valid.")
        else:
            print("Invalid name. Make sure it contains only letters and is properly capitalized.")
    elif detail == "address":
        if re.match(r"^[a-zA-Z0-9\s]+$", data):
            print("Address is valid.")
        else:
            print("Invalid address. Special characters are not allowed.")
    elif detail == "phone":
        if re.match(r"^\d{3}-\d{3}-\d{4}$", data):
            print("Phone number is valid.")
        else:
            print("Invalid phone number. Follow the format ###-###-####.")
    else:
        print("Invalid detail type.")

def format_address(street, city, state, zip_code):
    formatted_street = street.title()
    formatted_city = city.title()
    formatted_state = state.upper()
    formatted_zip = re.sub(r'[^0-9]', '', zip_code)
    
    print(f"Formatted Address: {formatted_street}, {formatted_city}, {formatted_state} - {formatted_zip}")

def generate_order_confirmation_email(customer_name, order_number, delivery_address, delivery_date):
    email = (f"Dear {customer_name},\n\n"
            f"Your order {order_number} has been placed successfully.\n"
            f"Delivery Address: {delivery_address}\n"
            f"Expected Delivery Date: {delivery_date}\n\n"
            "Thank you for shopping with us!")
    
    print("\nOrder Confirmation Email:\n")
    print(email)

def calculate_shipping_cost(distance, weight):
    cost = (distance * 0.5) + (weight * 0.2)
    print(f"Shipping cost is ${cost:.2f}")

def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(10))
    print(f"Generated Password: {password}")

def find_similar_addresses(addresses, target_address):
    similar_addresses = [address for address in addresses if target_address.lower() in address.lower()]
    if similar_addresses:
        print(f"Addresses similar to '{target_address}':")
        for address in similar_addresses:
            print(address)
    else:
        print("No similar addresses found.")

def menu():
    while True:
        print("\n--- Task 4: Menu ---")
        print("1. Parcel Tracking")
        print("2. Customer Data Validation")
        print("3. Address Formatting")
        print("4. Order Confirmation Email")
        print("5. Calculate Shipping Costs")
        print("6. Generate Password")
        print("7. Find Similar Addresses")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            parcel_tracking()
        elif choice == "2":
            data = input("Enter the data: ")
            detail = input("Is it a 'name', 'address', or 'phone'?: ")
            validate_customer_data(data, detail)
        elif choice == "3":
            street = input("Enter street: ")
            city = input("Enter city: ")
            state = input("Enter state: ")
            zip_code = input("Enter zip code: ")
            format_address(street, city, state, zip_code)
        elif choice == "4":
            customer_name = input("Enter customer name: ")
            order_number = input("Enter order number: ")
            delivery_address = input("Enter delivery address: ")
            delivery_date = input("Enter expected delivery date: ")
            generate_order_confirmation_email(customer_name, order_number, delivery_address, delivery_date)
        elif choice == "5":
            distance = float(input("Enter distance (in km): "))
            weight = float(input("Enter parcel weight (in kg): "))
            calculate_shipping_cost(distance, weight)
        elif choice == "6":
            generate_password()
        elif choice == "7":
            addresses = ["123 Main St, Springfield", "124 Main St, Springfield", "456 Oak St, Shelbyville"]
            target_address = input("Enter the address to search for similar addresses: ")
            find_similar_addresses(addresses, target_address)
        elif choice == "0":
            print("Exiting the APplication...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()
