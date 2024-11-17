def check_order_status(status):
    if status == "processing":
        print("Your order is being processed, please wait for further updates.")
    elif status == "delivered":
        print("Your order has been delievered, thank you :) ")
    elif status == "cancelled":
        print("Your order has been cancelled :( ")
    else:
        print("Enter Valid Status, please try again.")

def main():
    order_status = input("Enter Order Status(Processing, Delivered, Cancelled): ").lower()
    check_order_status(order_status)

main()
