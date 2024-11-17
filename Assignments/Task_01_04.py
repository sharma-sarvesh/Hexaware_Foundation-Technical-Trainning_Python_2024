
def assign_shipment(weight):
    if weight <= 0:
        print("Invalid input, weight must be greater than 0")
    elif weight <= 100:
        print("Shipment A is assigned to you")
    elif 100 < weight <= 500:
        print("Shipment B is assigned to you")
    else:  
        print("Shipment C is assigned to you")

def main():
    while True:
        try:
            courier_weight = float(input("Enter the weight of the courier(in kg), or type -1 to exit: "))
            
            # Exit the loop
            if courier_weight == -1:
                print("Exiting the system, Thank you!!!")
                break
            
            result = assign_shipment(courier_weight)
            if result is not None:
                print(result)
            
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

main()
