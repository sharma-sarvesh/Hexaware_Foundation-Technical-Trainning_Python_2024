
def categorize_parcel(wei):
    if wei < 0:
        print("Error, weight cannot be Negative")
    elif wei < 5:
        print(f"Your paracel of {wei} kg's is categorised as Light")
    elif 5 <= wei <= 10:
        print(f"Your paracel of {wei} kg's is categorised as Medium")
    elif wei > 10:
        print(f"Your paracel of {wei} kg's is categorised as Heavy")
    else:
        return "Invalid Weight"
    
def main():
    weight = float(input("Enter weight of parcel in kg's: "))
    categorize_parcel(weight)

main()
