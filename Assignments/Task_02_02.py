# while loop to track the real-time location of a courier until it reaches its destination. 

import time

def track_courier(destination):
    current_location = "Warehouse"
    while current_location != destination:
        print(f"Courier is currently at: {current_location}")

        if current_location == "Warehouse":
            current_location = "Distribution Center"
        elif current_location == "Distribution Center":
            current_location = "Local Depot"
        elif current_location == "Local Depot":
            current_location = destination  # Arrived at destination
        time.sleep(2)  # Simulate time taken to move to the next location
    print(f"Courier has arrived at: {destination}")


def main():
    track_courier("destination")

main()
