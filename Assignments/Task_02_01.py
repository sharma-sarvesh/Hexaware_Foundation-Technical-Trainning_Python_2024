# for loop to display all the orders for a specific customer. 


orders = [
    {"customer_id": 1, "order_id": 101, "order_status": "Delivered"},
    {"customer_id": 1, "order_id": 102, "order_status": "Processing"},
    {"customer_id": 2, "order_id": 201, "order_status": "Cancelled"},
    {"customer_id": 1, "order_id": 103, "order_status": "Delivered"},
    ]

def display_orders_for_customer(customer_id):
    flag = False
    print(f"Orders for Customer ID: {customer_id}")
    
    for order in orders:
        if order["customer_id"] == customer_id:
            print(f"Order ID: {order['order_id']}, Status: {order['order_status']}")
            flag = True
    
    return flag

def main():
    while True:
        customer_id = int(input("Enter Customer ID: "))
        if display_orders_for_customer(customer_id):
            break  # Exit loop if valid orders are found
        else:
            print("Please enter a valid customer ID")

main()

