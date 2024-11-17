# Modules - Python file - which has some variables, functions, class - That can be used inside other files

# Import method 1
import my_module # importing the module

my_module.greet()
my_module.greet_person("HRB")
person_1 = my_module.Person("Hiran Ram Babu")
person_1.greet_person()
print(my_module.company_name)
my_module.__intro()


# # Import method 2
# import my_module as baseM
# baseM.greet()

# # Import method 3
# from my_module import greet
# greet()

# # Import method 4
# from my_module import * # when we do not know what are the functions/class/variables available, still we need those
# # the above line will create namespace pollution

# Import from package
# import my_package
# from my_package import my_module1
# from my_package.my_module1 import greet_person
# from my_package.my_module1 import *



# standart modules & Packages - os, sys, math, random

import os, sys, math, random
print(os.getcwd())
print(sys.getwindowsversion())
print(math.sqrt(4))
print(random.randint(1,10))