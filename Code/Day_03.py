# 09-10-24

# DICTIONARY - key value - {} - mutuable(updatable) - unordered - indexed with keys - key should be unique, values can be of any data type

dict_1 = {
    'name' : 'SMS',
    'age' : 23,
    'hobbies' : ["Walk", "Gym", "Playing Games"],
    'worklocation' : ("Hyderabad", "Pune", 400101, 4316056),
    'skills' : {
        'Frontend' : 'React.JS',
        'Backend' : 'Python, Django',
        'Automation' : ['Python', 'Power Shell']
    }
}

print(dict_1)
print(dict_1['hobbies'])
print(dict_1['worklocation'])    # to access
print(dict_1.get('name'))    # fun to access

dict_1['mobile'] = 7248940124     #adding new key value pair
print(dict_1)

dict_1['age'] = 25
print(dict_1)   #value uupdation

print("**********")
del dict_1['age'] # removes specified key value paid but do not return anything
print(dict_1)

delMobile = dict_1.pop('mobile') # Removes specified key Value pair
print(delMobile)

delLast = dict_1.popitem() # Removes the last added key value pair
print(delLast)
print(dict_1)



print(dict_1.keys())
print(dict_1.values())
print(dict_1.items())
print(dict_1)

print("********************")

dict_2 = {
    'name' : 'SMS',
    'age' : 789456,
    'hobbies' : ["Walk", "Gym", "Playing Games"],
    'worklocation' : ("Hyderabad", "Pune", 400101, 4316056),
    'skills' : {
        'Frontend' : 'React.JS',
        'Backend' : 'Python, Django',
        'Automation' : ['Python', 'Power Shell']
    }
}

dict_1.update(dict_2)  #update dict_1 with values of dict_2
print(dict_1)

# looping through dictionary

for key, value in dict_1.items():
    print("{} has {}".format(key, value))



# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# inventory_management_system()


inventory = {
    "apple": [100, 0.5],
    "banana": [120, 0.3],
    "mango": [150, 0.8],
    "oraange": [140, 0.6]
}

# Step 2: Display the inventory
def display_inventory():
    print("Inventory:")
    for product, info in inventory.items():
        print(f"Product: {product}, Quantity: {info[0]}, Price: ${info[1]}")

# Step 3: Sell a product
def sell_product():
    product_name = input("Enter the product name you want to buy: ").lower()
    
    if product_name in inventory:
        quantity_in_stock = inventory[product_name][0]
        price_per_unit = inventory[product_name][1]
        
        try:
            quantity_to_buy = int(input(f"How many {product_name} you want to buy? "))
            
            if quantity_to_buy <= quantity_in_stock:
                total_cost = quantity_to_buy * price_per_unit
                inventory[product_name][0] -= quantity_to_buy
                print(f"Total cost: Rs.{total_cost}")
                print(f"{quantity_to_buy} {product_name} sold. New stock: {inventory[product_name][0]}")
            else:
                print(f"Not enough stock. Only {quantity_in_stock} {product_name}(s) available.")
        except ValueError:
            print("Please enter a valid quantity.")
    else:
        print(f"{product_name} is not available in the inventory.")

# Step 4: Restock a product
def restock_product():
    product_name = input("Enter the product name you want to restock: ").lower()
    
    if product_name in inventory:
        try:
            quantity_to_add = int(input(f"How many {product_name}(s) do you want to add to the stock? "))
            inventory[product_name][0] += quantity_to_add
            print(f"{product_name} stock updated. New stock: {inventory[product_name][0]}")
        except ValueError:
            print("Please enter a valid quantity.")
    else:
        print(f"{product_name} is not available in the inventory.")

# Main menu-driven application
def inventory_management_system():
    while True:
        print("\n1. Display Inventory\n2. Sell Product\n3. Restock Product\n4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_inventory()
        elif choice == "2":
            sell_product()
        elif choice == "3":
            restock_product()
        elif choice == "4":
            print("Exiting the inventory management system!!!")
            break
        else:
            print("Invalid choice, please choose again")

# Start the inventory management system
inventory_management_system()

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# DATE & TIME 
import datetime  #call complete  module in python
print(datetime.datetime.now())
        #OR 
from datetime import datetime   #call specific fun/class of a module - from module import function/class
print(datetime.now())

print(datetime.date.today())

print(datetime.datetime.now().strftime("%d-%m-%Y")) # format date time type

date_time = "2024-10-09 11:43:45"
print(type(date_time))

date_time_proper = datetime.datetime.strptime(date_time,"%Y-%m-%d %H:%M:%S") # Convert string to date time type

# print(type(datetime.datetime.strptime(date_time,"%Y-%m-%d %H:%M:%S"))) # Convert string to date time type

date_proper = date_time_proper.strftime("%d")
print("Current Date is",date_proper)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# FUNCTION - block of code which can be reusesd 

from datetime import datetime
import time

def greet_guests():
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print("HEy guest, thanks for coming!!!")
    print("You have been logged in at {}", current_time)


greet_guests()
time.sleep(5)
greet_guests()
time.sleep(5)
greet_guests()
time.sleep(4)
greet_guests()




from datetime import datetime
import time

def greet_guests(name = "guest"):
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print(f"HEy {name}, thanks for coming!!!")
    print(f"You have been logged in at {current_time}")


greet_guests("a")
time.sleep(5)
greet_guests("b")
time.sleep(5)
greet_guests()    #default guest will bve preinted
time.sleep(4)
greet_guests("d")



def addition_mul(*args): # * before the argument args shows it is a multi/variable length argument; This accepts only values; this behaves as a tuple
    result = 0
    for num in args:
        result += num
    return result


print(addition_mul(1,2,345,223,532,12,432))
print(addition_mul(56,33))
print(addition_mul(56,33,25,26,32))




def user_profile(**kwargs): # ** before the argument kwargs shows it is a multi/variable length keyword argument; This accepts key value pairs; this behaves as a dictionary    for key, value in kwargs.items():        print("{} has {}".format(key, value))user_profile(name="HRB", mobile=8825410600, city="Chennai")user_profile(name="Hiran Ram Babu", email="info@mjit.in", city="Chennai")



def user_profile(name,age,*args,**kwargs):    print("Name: {}".format(name))    print("Age: {}".format(age))    if args:        print("Args items:")        for val in args:            print(val)    if kwargs:        print("Kwargs items:")        for key, value in kwargs.items():            print("{}: {}".format(key, value))# user_profile("HRB",25, "BE EIE", "Indian", mobile=8825410600, city="Chennai")# user_profile("Hiran Ram Babu", 34, "KLNCE Student", "Automation Architect", email="info@mjit.in", city="Chennai")user_profile("Vignesh", 22, profession="Student", College="KLNCE")\




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








