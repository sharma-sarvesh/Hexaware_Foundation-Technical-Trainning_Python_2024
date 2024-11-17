# Task_03.py

import math

tracking_history = []
couriers = [
    {"courier_id": 1, "name": "Courier A", "location": (5, 5)},  # X, Y coordinates
    {"courier_id": 2, "name": "Courier B", "location": (2, 3)},
    {"courier_id": 3, "name": "Courier C", "location": (7, 8)},
    ]

def menu():
    print("\n ***** Courier Management System ***** ")
    print("1. Add Tracking History")
    print("2. Display Tracking History")
    print("3. Find Nearest Available Courier")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    return choice

def add_tracking_history():
    location = input("Enter new location update for the parcel('Warehouse','Distribution Center','Local Depot','Out for Delivery', 'Delivered to Customer'): ")
    tracking_history.append(location)
    print(f"Location '{location}' added to tracking history.")

def display_tracking_history():
    if len(tracking_history) == 0:
        print("No tracking history available.")
    else:
        print("Tracking History:")
        for index, location in enumerate(tracking_history):
            print(f"{index + 1}. {location}")

def calculate_distance(loc1, loc2):
    return math.sqrt((loc2[0] - loc1[0]) ** 2 + (loc2[1] - loc1[1]) ** 2)

def find_nearest_courier():
    user_x = float(input("Enter your X coordinate: "))
    user_y = float(input("Enter your Y coordinate: "))
    
    min_distance = float("inf")
    nearest_courier = None
    
    for courier in couriers:
        courier_location = courier["location"]
        distance = calculate_distance(courier_location, (user_x, user_y))
        if distance < min_distance:
            min_distance = distance
            nearest_courier = courier
    
    if nearest_courier:
        print(f"The nearest courier is {nearest_courier['name']} at location {nearest_courier['location']} with a distance of {min_distance:.2f} units.")
    else:
        print("No couriers available.")

# Main program loop
def main():
    while True:
        choice = menu()
        if choice == 1:
            add_tracking_history()
        elif choice == 2:
            display_tracking_history()
        elif choice == 3:
            find_nearest_courier()
        elif choice == 4:
            print("Exiting system.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
