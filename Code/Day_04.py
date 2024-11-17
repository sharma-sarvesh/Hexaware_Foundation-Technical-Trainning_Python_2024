# OOP - objects - Reusability
# Blueprint - 1; but multiple similar products
# Class - Blueprint - Always starts with capital case
    # Attributes - Properties - variables - definesa the class
    # Methods/Functions - Actions/Activity it can perform - behavious of class
# Objects - instances
#Access
# inheritance
# Polymorphism
# Composition
# Abstraction
# Encapsulation
# Method Overriding
# class ClassName:
    # var1 = Val1

    # def method_1(self):
        # statements/expr/returns/pass

# Obj1 = ClassName()
# self - positional attribute - if i need to access attribute, I need self at 1st position (self is not mandate keyword)

# Class defination
class Car:
    model = "Altroz"    #Attribute

    def display_details(self):    #MEthod
        print(f"This is car with model {self.model}")

my_car = Car()            #Object creation
my_car.display_details()    #Access of Class Attributes & Methods

# Class defination
class Car:
    def __init__(self, model, color):     #Constructor - automatically initialises when creating any object 
        self.model = model    
        self.color = color

    def display_details(self):    #MEthod - Public
        print(f"This is car with model {self.model} & {self.color} color")

my_car = Car("AUDI", "White")            #Object creation
my_car.display_details()    #Access of Class Attributes & Methods
print(my_car.model)     # accessing public attribute
print(my_car.color)     # accessing public attribute


# ACCESS sPECIFIERS - WHAT AN OBJ CAN ACCESS FROM THE CLASS
#Public - default - can be accessed anywhere wihin or outside the class 
#Preotected - defined with _ as prefix - accessed within class, subclass, obj(not recommended)
#Private - defined with __ as prefix - accessed only within class

# Public
class Car:
    def __init__(self, model, color):     #Constructor - automatically initialises when creating any object 
        self.model = model    
        self.color = color

    def display_details(self):    #MEthod - Public
        print(f"This is car with model {self.model} & {self.color} color")

my_car = Car("AUDI", "White")            #Object creation
my_car.display_details()    #Access of Class Attributes & Methods
print(my_car.model)     # accessing public attribute
print(my_car.color)     # accessing public attribute


# Protected
class Car:
    def __init__(self, model, color):     #Constructor - automatically initialises when creating any object 
        self.model = model     #Accessing Public Attribute
        self._color = color    #Accessing Protected Attribute

    def display_details(self):    #MEthod - Public
        print(f"This is car with model {self.model} & {self._color} color")

my_car = Car("AUDI", "White")            #Object creation
my_car.display_details()    #Access of Class Attributes & Methods
print(my_car.model)     # accessing public attribute
print(my_car._color)     # accessing protected attribute (NOT RECOMMENDED)

# Private
class Car:
    def __init__(self, model, color):     #Constructor - automatically initialises when creating any object 
        self.model = model     #Accessing Public Attribute
        self.__color = color    #Accessing Private Attribute

    def display_details(self):    #MEthod - Public
        print(f"This is car with model {self.model} & {self.__color} color")

my_car = Car("AUDI", "White")            #Object creation
my_car.display_details()    #Access of Class Attributes & Methods
print(my_car.model)     # accessing public attribute
print(my_car.__color)     # accessing private attribute - ERROR
                        #AttributeError: 'Car' object has no attribute '__color'


#Inheritance - child class inherit data & methods from parent class
# we can only inherit when there is relation between parent & child class
'''
Single: 1 parent
Multiple: nore than 1 parent
Multilevel: parent - child - sub child...
Hierarchiaal: 1 parent - multi child - like a tree structure
Hybrid: mix of the above
'''

# class ParentClass:
    #pass

# class ChildClass(ParentClass):
    #pass

# Single Inheritance

class Vehicle:
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

    def start(self):
        print(f"{self.manufacturer} vehicle is started!")

class Car(Vehicle):
    def __init__(self, manufacturer, model, color):
        super().__init__(manufacturer)      # super() - to call from parent class
        self.model = model
        self.color = color
    
    def display_details(self):
        print(f"This is car with model {self.model} & it's color {self.color}")

sample_vehicle = Vehicle("Tata")    #obj1 - using class vehicle
sample_vehicle.start()

my_car = Car("Audi", "Q5", "Red") #obj2 - using child class car
my_car.start()              #inherited from parent class
my_car.display_details()    #inherited from child class 

# Multiple Inheritance
class Vehicle:
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer
    
    def start(self):
        print("{} vehicle is started!".format(self.manufacturer))

class Product():
    def __init__(self, regNum):
        self.regNum = regNum

    def product_details(self):
        print("This car is having an registration number of {}".format(self.regNum))

class Car(Vehicle, Product):
    def __init__(self, manufacturer, regNum, model, color):
        # super().__init__(manufacturer, regNum)
        # super().__init__(regNum)
        Vehicle.__init__(self, manufacturer)
        Product.__init__(self, regNum)
        self.model = model
        self.__color = color

    def display_details(self): # Method - public
        print("This is Car from {} with model {} and its {} with a registration number as {}".format(self.manufacturer, self.model, self.__color, self.regNum)) #Action the method going to perform

sample_vehicle = Vehicle("Tata") # Object 1 - using class Vehicle
sample_vehicle.start()

my_car = Car("Hundai", "AB 45 C 2345", "i20", "Red") # Object 2 - using child class Car
my_car.start() # inherited method from parent class
my_car.product_details()
my_car.display_details() # method from child class


# Multi Level Inheritance
class Vehicle:
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer
    
    def start(self):
        print("{} vehicle is started!".format(self.manufacturer))

class Car(Vehicle):
    def __init__(self, manufacturer,model, color):
        super().__init__(manufacturer)
        self.model = model
        self.__color = color

    def display_details(self): # Method - public
        print("This is Car from {} with model {} and its {}".format(self.manufacturer, self.model, self.__color)) #Action the method going to perform

class ElectricCar(Car):
    def __init__(self, manufacturer, model, color, batter_capacity):
        super().__init__(manufacturer, model, color)
        self.batter_capacity = batter_capacity
    
    def display_battery_details(self):
        print("This is an Electric car with a capacity of {} kWh".format(self.batter_capacity))

sample_vehicle = Vehicle("Tata") # Object 1 - using class Vehicle
sample_vehicle.start()

my_car = ElectricCar("Hundai", "i20", "Red", 150) # Object 2 - using child class Car
my_car.start() # inherited method from parent class
my_car.display_details() # method from child class
my_car.display_battery_details()


# Hierarchiaal Level Inheritance
class Vehicle:
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer
    
    def start(self):
        print("{} vehicle is started!".format(self.manufacturer))

class Car(Vehicle):
    def __init__(self, manufacturer,model, color):
        super().__init__(manufacturer)
        self.model = model
        self.__color = color

    def display_details(self): # Method - public
        print("This is Car from {} with model {} and its {}".format(self.manufacturer, self.model, self.__color)) #Action the method going to perform

class Bike(Vehicle):
    def __init__(self, manufacturer, bike_type):
        super().__init__(manufacturer)
        self.bike_type = bike_type
    
    def display_bike_details(self):
        print("This is Bike from {} with type {}".format(self.manufacturer, self.bike_type)) #Action the method going to perform


my_car = Car("Hundai", "i20", "Red") # Object 2 - using child class Car
my_car.start() # inherited method from parent class
my_car.display_details() # method from child class

my_bike = Bike("Bajaj", "Avenger 220 Cruise") # Object 2 - using child class Car
my_bike.start() # inherited method from parent class
my_bike.display_bike_details() # method from child class


# Hybrid Inheritance
class Vehicle:
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer
    
    def start(self):
        print("{} vehicle is started!".format(self.manufacturer))

class Product():
    def __init__(self, regNum):
        self.regNum = regNum

    def product_details(self):
        print("This car is having an registration number of {}".format(self.regNum))

class Car(Vehicle, Product):
    def __init__(self, manufacturer, regNum, model, color):
        Vehicle.__init__(self, manufacturer)
        Product.__init__(self, regNum)
        self.model = model
        self.__color = color

    def display_details(self): # Method - public
        print("This is Car from {} with model {} and its {} with a registration number as {}".format(self.manufacturer, self.model, self.__color, self.regNum)) #Action the method going to perform

class ElectricCar(Car):
    def __init__(self, manufacturer, regNum, model, color, batter_capacity):
        super().__init__(manufacturer, model, regNum, color)
        self.batter_capacity = batter_capacity
    
    def display_battery_details(self):
        print("This is an Electric car with a capacity of {} kWh".format(self.batter_capacity))

class Bike(Vehicle):
    def __init__(self, manufacturer, bike_type):
        super().__init__(manufacturer)
        self.bike_type = bike_type
    
    def display_bike_details(self):
        print("This is Bike from {} with type {}".format(self.manufacturer, self.bike_type)) #Action the method going to perform


my_car = Car("Hundai", "AB 33 C 4567", "i20", "Red") # Object 2 - using child class Car
my_car.start() # inherited method from parent class
my_car.display_details() # method from child class

my_bike = Bike("Bajaj", "Avenger 220 Cruise") # Object 2 - using child class Car
my_bike.start() # inherited method from parent class
my_bike.display_bike_details() # method from child class

my_car1 = ElectricCar("Hundai", "XY 12 Z 9876", "i20", "Red", 150) # Object 2 - using child class Car
my_car1.start() # inherited method from parent class
my_car1.display_details() # method from child class
my_car1.display_battery_details()



# *******************************************************************
# * Polymorphism - one method many forms - over riding 
# Method Overriding - override a method depend on object or where it is being called

 
# Polymorphism - many forms - same method - based on the object - Over riding
# Method Overriding - Override a method depends on the object or where it is being called

class Vehicle:
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer
    
    def start(self):
        print("{} vehicle is started!".format(self.manufacturer))

class Product():
    def __init__(self, regNum):
        self.regNum = regNum
    def product_details(self):
        print("This car is having an registration number of {}".format(self.regNum))

class Car(Vehicle, Product):
    def __init__(self, manufacturer, regNum, model, color):
        Vehicle.__init__(self, manufacturer)
        Product.__init__(self, regNum)
        self.model = model
        self.__color = color
    def display_details(self): # Method - public
        print("This is Car from {} with model {} and its {} with a registration number as {}".format(self.manufacturer, self.model, self.__color, self.regNum)) #Action the method going to perform
    def start(self):
        print("{} vehicle Roars!".format(self.manufacturer))

class ElectricCar(Car):
    def __init__(self, manufacturer, regNum, model, color, batter_capacity):
        super().__init__(manufacturer, model, regNum, color)
        self.batter_capacity = batter_capacity
    
    def display_battery_details(self):
        print("This is an Electric car with a capacity of {} kWh".format(self.batter_capacity))
    
    def start(self):
        print("{} vehicle is silently starts!".format(self.manufacturer))

class Bike(Vehicle):
    def __init__(self, manufacturer, bike_type):
        super().__init__(manufacturer)
        self.bike_type = bike_type
    
    def display_bike_details(self):
        print("This is Bike from {} with type {}".format(self.manufacturer, self.bike_type)) #Action the method going to perform
    
    def start(self):
        print("{} vehicle vrooms!".format(self.manufacturer))

sample_vehicle = Vehicle("Tata") # Object 1 - using class Vehicle
sample_vehicle.start()
my_car = Car("Hundai", "AB 33 C 4567", "i20", "Red") # Object 2 - using child class Car
my_car.start() # inherited method from parent class
my_car.display_details() # method from child class
my_bike = Bike("Bajaj", "Avenger 220 Cruise") # Object 2 - using child class Car
my_bike.start() # inherited method from parent class
my_bike.display_bike_details() # method from child class
my_car1 = ElectricCar("Hundai", "XY 12 Z 9876", "i20", "Red", 150) # Object 2 - using child class Car
my_car1.start() # inherited method from parent class
my_car1.display_details() # method from child class
my_car1.display_battery_details()




# *******************************************************************
# * Access Specifiers/Modifiers for methods

class Vehicle:
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer
    
    def start(self):
        print("{} vehicle is started!".format(self.manufacturer))

    def _protected_method(self):  # Protected method
        print("{} vehicle has a protected method!".format(self.manufacturer))
    
    def __private_method(self):  # Private method
        print("{} vehicle has a private method!".format(self.manufacturer))
    
    def access_private_method(self):  # Public method to access private method
        self.__private_method()

class Product():
    def __init__(self, regNum):
        self.regNum = regNum

    def product_details(self):
        print("This car is having an registration number of {}".format(self.regNum))

class Car(Vehicle, Product):
    def __init__(self, manufacturer, regNum, model, color):
        Vehicle.__init__(self, manufacturer)
        Product.__init__(self, regNum)
        self.model = model
        self.__color = color

    def display_details(self): # Method - public
        print("This is Car from {} with model {} and its {} with a registration number as {}".format(self.manufacturer, self.model, self.__color, self.regNum)) #Action the method going to perform

    def start(self):
        print("{} vehicle Roars!".format(self.manufacturer))
        self._protected_method()  # Accessing protected method
        # self.__private_method() # will throw error
        self.access_private_method()  # Accessing private method

sample_vehicle = Vehicle("Tata") # Object 1 - using class Vehicle
sample_vehicle.start()

my_car = Car("Hundai", "AB 33 C 4567", "i20", "Red") # Object 2 - using child class Car
my_car.start() # inherited method from parent class
my_car.display_details() # method from child class
# my_car.__private_method() # throws error as we cannot access the private methods outside class
my_car._protected_method() # not recommended
my_car.access_private_method()


# *******************************************************************
#* Composition - similar to inheritance but needs to have a relationship

class Engine:
    def __init__(self, hp):
        self.hp = hp
    def start(self):
        print("Engine with {} HP is starting!".format(self.hp))

class Vehicle:
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer
    
    def start(self):
        print("{} vehicle is started!".format(self.manufacturer))

class Car(Vehicle):
    def __init__(self, manufacturer, model, color, hp):
        super().__init__(manufacturer)
        self.model = model
        self.__color = color
        self.engine = Engine(hp)

    def display_details(self): # Method - public
        print("This is Car from {} with model {} and its {}".format(self.manufacturer, self.model, self.__color)) #Action the method going to perform
        self.engine.start()

sample_vehicle = Vehicle("Tata") # Object 1 - using class Vehicle
sample_vehicle.start()

my_car = Car("Hundai", "i20", "Red", 18) # Object 2 - using child class Car
my_car.start() # inherited method from parent class
my_car.display_details() # method from child class


# *******************************************************************
#*       FILE HANDLING

# File Handling - Handling and Manipulating the files
# human readble form or non-human readable form.
# Text files and Binary Files
# File needs to be available
# Open the file - open() - w, r, r+, a, x, rw
# Read the file - read(), readline(), readlines()
# Write in the File - write(), writelines()
# Apped the file
# close the file (Important activity to perform) - close()

# Open the file
file = open('test.txt', 'w')
# file = open('test.txt', 'r')
# file = open('test.txt', 'r+w')

# Write date to the file
file.write("Hey World!")
file.write("Welcome to hexaware Session!!")

# close the file
file.close()

file = open('test.txt', 'r')
file_content = file.read()
print(file_content)
#file.close()

file = open('test.txt', 'a')
file.write("\nI have appended this line")
file.close()


# with Context Manager - with statement - this auto closes the file
with open('test.txt', 'r') as file:
    file_content = file.read()
    print(file_content)



