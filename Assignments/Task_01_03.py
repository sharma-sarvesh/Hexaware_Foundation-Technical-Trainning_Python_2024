
def authenticate_user(username, password):
    user_data = {           #username: password
        "SMS": "emp_sms",
        "MYM": "emp_mym",
        "JDA": "emp_jda",
        "INS": "emp_ins",
    }

    if username in user_data:
        if user_data[username] == password:
            print(f"Login successful! Welcome, {username}.") 
        else:
            print("Incorrect password, Please try again.")
    else:
        return "Username not found, please check your credentials."

def main():

    username = input("Enter your username: ")
    password = input("Enter your password: ")
    result = authenticate_user(username, password)
    print(result)

main()
