<<<<<<< HEAD
# 08-10-24

'''
python case sensitive
var1 or Var1 or VAR1 are different
variable/funcrtion - snakle case - my_var1; get_details(),
Class - CamelCase
'''

name = "Sarvesh"
_mobile = 7248940124
email_id = "sarvesh9075@gmail.com"

print(name)
print(_mobile)
print(email_id)

'''
numeric - int,ffloat,compolex 
sequence - sequence of char,values
mapping - key value pairs - ictionary
set - kind of qsequence
boolean - True or False
'''

int_1 = 10
float_1 = 10.5
comp_1 = 3+4j
list_1 = [1,2,"SMS"]
tuple_1 = (1,2,"SMS")

# dict_1 = {
#     "Name" = "SMS",
#     "mob" = 7248940124
# }

set_1 = {1,2,"SMS"}

is_active = True

print(type(int_1))
print(type(float_1))
print(type(comp_1))
print(type(name))
print(type(list_1))
print(type(tuple_1))
#print(type(dict_1))
print(type(set_1))
print(type(is_active))


#name_2 = input("Enter your Name: ")
name_2 = "SARVESH"
print(name_2)


# Output Formating
# print(name)
print("Entered Name is" + name_2) # Concatination Operator +; Only similar data type can be handled/concatenated or only strings
print("Entered Name is: " + name_2) #Entered Name is: jkl
print("Entered Name is", name_2) # multi value output; any datatype, any values can be concatenated, but it is little tricy to manage the output display
print("Entered Name is {}".format(name_2)) # built in format function; similar to multi value but will look very simple for long output displays

# print("The entered name is " + name_2 + "With an id of " + int_1 + ". also has an email address mapped as " + email_id ) # We cannot concate str and Int
print("The entered name is", name_2, "With an id of", int_1, ". also has an email address mapped as", email_id )
print("The entered name is {} With an id of {}, also has an email address mapped as {}".format(name_2,int_1, email_id) )

# print("The entered name is " + name_2 + "With an id of " + int_1 + ". also has an email address mapped as " + email_id ) # We cannot concate str and Int
# import sys
# print("This is correct", file=sys.stderr)
# sys.stderr.write("This is correct")

'''
OPERATORS

Arithmetic: + = * / % **
Comaprision: > < >= <= == !=
Logical: and or not
Assignment: = += -=
Membership: in, not in 
iDENTITY: is, is not
'''
int_1 = 10
int_2 = 5

print("Arithmetic Operator")
print(int_1 + int_2)
print(int_1 - int_2)
print(int_1 * int_2)
print(int_1 / int_2)
print(int_1 % int_2)

print("Comparision Operator")
print(int_1 > int_2)  #True
print(int_1 < int_2)  #False
print(int_1 == int_2) #False

print("Logical Operator")
bool_1 = True
bool_2 = False

print(bool_1 and bool_2) #False
print(bool_1 or bool_2)  #True
print(not bool_1)        #False

print(int_1 > int_2) and not(int_1 == int_2)

print("Membership Operator")
print('H' in name)
print(1 in list_1)

print("Identity Operator")
print(name)    #Sarvesh
print(name_2)  #SARVESH
print("name is name_2:", name is name_2)       #False
print(int_1 is not float_1) #True


# TASK
stu_name = input("Enter Student's Name: ")
mob_no = input("Enter Student's Mobile No.: ")
stu_marks = input("Enter Marks: ")

print("\t** Student Details: **")
print("Name          : ", stu_name)
print("Mobile No.    : ", mob_no)
print("Marks Obtained: ", stu_marks)

'''
STATEMENTS - control structures
indentation - tab/space before line
if
if else
if else ladder
if elif else
'''

i1 = 10
i2 = 20

if i1 > i2:         # : os mandatory to start the block
    print(f"{i1} is greater than {i2}", i1,i2)

if i1 > i2:         # : os mandatory to start the block
    print(f"{i1} is greater than {i2}", i1,i2)
else:
    print(f"{i2} might be greater")

if i1 > i2:         # : os mandatory to start the block
    print(f"{i1} is greater than {i2}")
elif i2 > i1:
    print(f"{i2} is greater than {i1}")
else:
    print("i1 and i2 are equal")



no = int(input("Enter a no.: "))

if no % 3 == 0:
    print(f"{no} is divisible by 3 & output is:", no/3)
else:
    print(f"{no} is not divisible by 3")


'''
LOOPS - iterations - 
while - indefinite -  we need to handel the input for failure of condition
for - definite - 
'''

counter = 1
iterations = 5
while counter <= iterations:
    print("Welcome to Hexaware :)")
    counter += 1     # counter = counter + 1

# range(start, end)
for counter in range(5,7):
    print("Welcome to Hexaware Python Batch") 



name = input("Enter Name: ")
wei = int(input("Enter Weight in kg: "))
hei = float(input("Enter Height in meter: " ))
# BMI = wei/hei**2
print("BMI: ", BMI)
if BMI <= 18.4:
    print(f"{name} your BMI is Underweight")
elif 18.5 < BMI < 24.9:
    print(f"{name}, your BMI is Normal")
elif 25.0 <= BMI <= 39.9:
    print(f"{name}, your BMI is Overweight")
else:
    print(f"{name}, your BMI is Obese")

flag = 1
while (flag == 1):
    name = input("Enter Name: ")
    wei = int(input("Enter Weight in kg: "))
    hei = float(input("Enter Height in meter: " ))

    BMI = wei/hei**2
    print("BMI: ", BMI)
    if BMI <= 18.4:
        print(f"{name} your BMI is Underweight")
    elif 18.5 < BMI < 24.9:
        print(f"{name}, your BMI is Normal")
    elif 25.0 <= BMI <= 39.9:
        print(f"{name}, your BMI is Overweight")
    else:
        print(f"{name}, your BMI is Obese")
    flag = int(input("Enter 1 to continue OR Enter 0 to exit: "))



import random
random_number = random.randint(1,50)
counter = 0

while True:
    print(random_number)
    no = int(input("Enter a random no between 1 to 50: ")) 
    if no > random_number:
        print("Too High")
    elif no < random_number:
        print("Too low")
    else:
        print("Correct Guess, congratlations!!")
        print(f"You took {counter} attempts")
        break
    counter += 1


# ATM Simulator
balance = 500
while True:
    print("\n\t***Hello, Welcome to ATM Simulator*** \nEnter 1 to Check balance \nEnter 2 to Withdraw Money \nEnter 3 to Deposit Money \nEnter 4 to Exit")
    inp = int(input("Enter Input: "))

    if inp == 1:
        print("\nCurrent Balance is: ",balance)
    
    elif inp == 2:
        wa = int(input("\nEnter Amount to Withdraw: "))
        if wa > balance:
            print("Insufficient Funds")
        else:
            balance -= wa
            print(f"{wa} amount withdrawn, available balance is {balance}")
    
    elif inp == 3:
        da = int(input("\nEnter Amount to Deposit: "))
        if da <= 0:
            print("Enter Valid Amount")
        else:
            balance += da
            print(f"{da} amount deposited, available balance is {balance}")

    elif inp == 4:
        print("\nEnd of Application!!!")
        break
    else:
        print("Enter Valid Input")


'''
list[] - array - ordered - allow duplicate - mutable(can be updatesd) - list[]
tuple() - array - ordered - allow duplicate - immutable(cannot be updated) - tuple()
set{} - array - unordered - will not allow duplicate - mutable - set{}
'''
list_1 = [1,2,3,4, "Hello", [6,7]]
tuple_1 = (1,2,3,4, "Hello", [6,7])
set_1 = {1,2,3,4, "Hello", [6,7]}

print(list_1)
print(tuple_1)
print(set_1)


# print(set_1[3])
 
list_1[3] = 3
# tuple_1[3] = 3
print(tuple_1.count(2))
print(tuple_1.index(2))
print(len(list_1))
print(len(tuple_1))
print(len(set_1))
print(set_1)
 
set_1.add(76)
print(set_1)
set_1.pop()
print(set_1)
set_1.remove(5)
print(set_1)

# LIST

list_1.append("Happy")
print(list_1)
list_1.insert(2, "Happy")
print(list_1)
list_1.extend(["Diwali", 88, 21])
print(list_1)
list_1.sort()
print(list_1)
list_1.reverse()
print(list_1)

print(list_1[1:3])
print(list_1[:4])
print(list_1[2:])


# STRINGS

str_1 = "Hello"
str_2 = "World"
str_3 = str_1 + str_2           #HelloWorld  
str_4 = str_1, str_2        # ('Hello', 'World')    forms a tuple
str_5 = str_1 + ' ' + str_2  #Hello World

print(str_3)
print(str_4)
print(type(str_4))
print(str_5)

print(str_5[4])
print(str_5[2:6])   
print(str_5[5:])        # World
print(str_5[:3])        #Hel
print(str_5 + "-----") #Hello World-----

print(len(str_5))
print(str_5.strip()+"---")
print(str_5.capitalize())
print(str_5.find('!'))
print(str_5.index('l'))
print(str_5.lower())
print(str_5.upper())
print(str_5.replace('World', "Hexaware"))
print(str_5.split())
print(str_5.zfill(15))           # fills space with 0 will len = 15
print("str_5: "str_5)
print("Replaced String: "str_5.replace('World', "Hexaware"))
print("str_5: "str_5)

str_5 = "Hello World"
print("str_5: ",str_5)    #Hello World    STRINGS are IMMUTABLE
print("Replaced String: ", str_5.replace('World', "Hexaware"))  #Hello Hexaware
print("str_5: ",str_5)  # Hello World --- string can be replaced but doesn't get stores



# Maths Functons
int_1 = 10
int_2 = 5

int_3 = int_1 + int_2
print(int_3)
print(type(float(int_3)))
print(int_3.is_integer())
=======
# 08-10-24

'''
python case sensitive
var1 or Var1 or VAR1 are different
variable/funcrtion - snakle case - my_var1; get_details(),
Class - CamelCase
'''

name = "Sarvesh"
_mobile = 7248940124
email_id = "sarvesh9075@gmail.com"

print(name)
print(_mobile)
print(email_id)

'''
numeric - int,ffloat,compolex 
sequence - sequence of char,values
mapping - key value pairs - ictionary
set - kind of qsequence
boolean - True or False
'''

int_1 = 10
float_1 = 10.5
comp_1 = 3+4j
list_1 = [1,2,"SMS"]
tuple_1 = (1,2,"SMS")

# dict_1 = {
#     "Name" = "SMS",
#     "mob" = 7248940124
# }

set_1 = {1,2,"SMS"}

is_active = True

print(type(int_1))
print(type(float_1))
print(type(comp_1))
print(type(name))
print(type(list_1))
print(type(tuple_1))
#print(type(dict_1))
print(type(set_1))
print(type(is_active))


#name_2 = input("Enter your Name: ")
name_2 = "SARVESH"
print(name_2)


# Output Formating
# print(name)
print("Entered Name is" + name_2) # Concatination Operator +; Only similar data type can be handled/concatenated or only strings
print("Entered Name is: " + name_2) #Entered Name is: jkl
print("Entered Name is", name_2) # multi value output; any datatype, any values can be concatenated, but it is little tricy to manage the output display
print("Entered Name is {}".format(name_2)) # built in format function; similar to multi value but will look very simple for long output displays

# print("The entered name is " + name_2 + "With an id of " + int_1 + ". also has an email address mapped as " + email_id ) # We cannot concate str and Int
print("The entered name is", name_2, "With an id of", int_1, ". also has an email address mapped as", email_id )
print("The entered name is {} With an id of {}, also has an email address mapped as {}".format(name_2,int_1, email_id) )

# print("The entered name is " + name_2 + "With an id of " + int_1 + ". also has an email address mapped as " + email_id ) # We cannot concate str and Int
# import sys
# print("This is correct", file=sys.stderr)
# sys.stderr.write("This is correct")

'''
OPERATORS

Arithmetic: + = * / % **
Comaprision: > < >= <= == !=
Logical: and or not
Assignment: = += -=
Membership: in, not in 
iDENTITY: is, is not
'''
int_1 = 10
int_2 = 5

print("Arithmetic Operator")
print(int_1 + int_2)
print(int_1 - int_2)
print(int_1 * int_2)
print(int_1 / int_2)
print(int_1 % int_2)

print("Comparision Operator")
print(int_1 > int_2)  #True
print(int_1 < int_2)  #False
print(int_1 == int_2) #False

print("Logical Operator")
bool_1 = True
bool_2 = False

print(bool_1 and bool_2) #False
print(bool_1 or bool_2)  #True
print(not bool_1)        #False

print(int_1 > int_2) and not(int_1 == int_2)

print("Membership Operator")
print('H' in name)
print(1 in list_1)

print("Identity Operator")
print(name)    #Sarvesh
print(name_2)  #SARVESH
print("name is name_2:", name is name_2)       #False
print(int_1 is not float_1) #True


# TASK
stu_name = input("Enter Student's Name: ")
mob_no = input("Enter Student's Mobile No.: ")
stu_marks = input("Enter Marks: ")

print("\t** Student Details: **")
print("Name          : ", stu_name)
print("Mobile No.    : ", mob_no)
print("Marks Obtained: ", stu_marks)

'''
STATEMENTS - control structures
indentation - tab/space before line
if
if else
if else ladder
if elif else
'''

i1 = 10
i2 = 20

if i1 > i2:         # : os mandatory to start the block
    print(f"{i1} is greater than {i2}", i1,i2)

if i1 > i2:         # : os mandatory to start the block
    print(f"{i1} is greater than {i2}", i1,i2)
else:
    print(f"{i2} might be greater")

if i1 > i2:         # : os mandatory to start the block
    print(f"{i1} is greater than {i2}")
elif i2 > i1:
    print(f"{i2} is greater than {i1}")
else:
    print("i1 and i2 are equal")



no = int(input("Enter a no.: "))

if no % 3 == 0:
    print(f"{no} is divisible by 3 & output is:", no/3)
else:
    print(f"{no} is not divisible by 3")


'''
LOOPS - iterations - 
while - indefinite -  we need to handel the input for failure of condition
for - definite - 
'''

counter = 1
iterations = 5
while counter <= iterations:
    print("Welcome to Hexaware :)")
    counter += 1     # counter = counter + 1

# range(start, end)
for counter in range(5,7):
    print("Welcome to Hexaware Python Batch") 



name = input("Enter Name: ")
wei = int(input("Enter Weight in kg: "))
hei = float(input("Enter Height in meter: " ))
# BMI = wei/hei**2
print("BMI: ", BMI)
if BMI <= 18.4:
    print(f"{name} your BMI is Underweight")
elif 18.5 < BMI < 24.9:
    print(f"{name}, your BMI is Normal")
elif 25.0 <= BMI <= 39.9:
    print(f"{name}, your BMI is Overweight")
else:
    print(f"{name}, your BMI is Obese")

flag = 1
while (flag == 1):
    name = input("Enter Name: ")
    wei = int(input("Enter Weight in kg: "))
    hei = float(input("Enter Height in meter: " ))

    BMI = wei/hei**2
    print("BMI: ", BMI)
    if BMI <= 18.4:
        print(f"{name} your BMI is Underweight")
    elif 18.5 < BMI < 24.9:
        print(f"{name}, your BMI is Normal")
    elif 25.0 <= BMI <= 39.9:
        print(f"{name}, your BMI is Overweight")
    else:
        print(f"{name}, your BMI is Obese")
    flag = int(input("Enter 1 to continue OR Enter 0 to exit: "))



import random
random_number = random.randint(1,50)
counter = 0

while True:
    print(random_number)
    no = int(input("Enter a random no between 1 to 50: ")) 
    if no > random_number:
        print("Too High")
    elif no < random_number:
        print("Too low")
    else:
        print("Correct Guess, congratlations!!")
        print(f"You took {counter} attempts")
        break
    counter += 1


# ATM Simulator
balance = 500
while True:
    print("\n\t***Hello, Welcome to ATM Simulator*** \nEnter 1 to Check balance \nEnter 2 to Withdraw Money \nEnter 3 to Deposit Money \nEnter 4 to Exit")
    inp = int(input("Enter Input: "))

    if inp == 1:
        print("\nCurrent Balance is: ",balance)
    
    elif inp == 2:
        wa = int(input("\nEnter Amount to Withdraw: "))
        if wa > balance:
            print("Insufficient Funds")
        else:
            balance -= wa
            print(f"{wa} amount withdrawn, available balance is {balance}")
    
    elif inp == 3:
        da = int(input("\nEnter Amount to Deposit: "))
        if da <= 0:
            print("Enter Valid Amount")
        else:
            balance += da
            print(f"{da} amount deposited, available balance is {balance}")

    elif inp == 4:
        print("\nEnd of Application!!!")
        break
    else:
        print("Enter Valid Input")


'''
list[] - array - ordered - allow duplicate - mutable(can be updatesd) - list[]
tuple() - array - ordered - allow duplicate - immutable(cannot be updated) - tuple()
set{} - array - unordered - will not allow duplicate - mutable - set{}
'''
list_1 = [1,2,3,4, "Hello", [6,7]]
tuple_1 = (1,2,3,4, "Hello", [6,7])
set_1 = {1,2,3,4, "Hello", [6,7]}

print(list_1)
print(tuple_1)
print(set_1)


# print(set_1[3])
 
list_1[3] = 3
# tuple_1[3] = 3
print(tuple_1.count(2))
print(tuple_1.index(2))
print(len(list_1))
print(len(tuple_1))
print(len(set_1))
print(set_1)
 
set_1.add(76)
print(set_1)
set_1.pop()
print(set_1)
set_1.remove(5)
print(set_1)

# LIST

list_1.append("Happy")
print(list_1)
list_1.insert(2, "Happy")
print(list_1)
list_1.extend(["Diwali", 88, 21])
print(list_1)
list_1.sort()
print(list_1)
list_1.reverse()
print(list_1)

print(list_1[1:3])
print(list_1[:4])
print(list_1[2:])


# STRINGS

str_1 = "Hello"
str_2 = "World"
str_3 = str_1 + str_2           #HelloWorld  
str_4 = str_1, str_2        # ('Hello', 'World')    forms a tuple
str_5 = str_1 + ' ' + str_2  #Hello World

print(str_3)
print(str_4)
print(type(str_4))
print(str_5)

print(str_5[4])
print(str_5[2:6])   
print(str_5[5:])        # World
print(str_5[:3])        #Hel
print(str_5 + "-----") #Hello World-----

print(len(str_5))
print(str_5.strip()+"---")
print(str_5.capitalize())
print(str_5.find('!'))
print(str_5.index('l'))
print(str_5.lower())
print(str_5.upper())
print(str_5.replace('World', "Hexaware"))
print(str_5.split())
print(str_5.zfill(15))           # fills space with 0 will len = 15
print("str_5: "str_5)
print("Replaced String: "str_5.replace('World', "Hexaware"))
print("str_5: "str_5)

str_5 = "Hello World"
print("str_5: ",str_5)    #Hello World    STRINGS are IMMUTABLE
print("Replaced String: ", str_5.replace('World', "Hexaware"))  #Hello Hexaware
print("str_5: ",str_5)  # Hello World --- string can be replaced but doesn't get stores



# Maths Functons
int_1 = 10
int_2 = 5

int_3 = int_1 + int_2
print(int_3)
print(type(float(int_3)))
print(int_3.is_integer())
>>>>>>> 2038cbd43d28caef807f4f8d4b50fb2ee88c917b
