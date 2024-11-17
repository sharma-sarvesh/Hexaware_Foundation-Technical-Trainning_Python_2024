# pytest | unittest
# pytest - testing framework
# /
# - app
# -- main.py
# - tests
# -- test_file.py
# test function:
# def test_function():
#   assert add(1,1) == 2 # assert - check or validate the result of add() with value in the right of ==
# Execute the following from the parent folder
# pytest - execute all the files under tests directory
# pytest tests/test_file.py - execute only the test_file.py
# pytest tests/test_file.py::test_function - execute only the test_function of test_file.py
# pytest -k 'funct' - execute all the matching functions which has the keyword 'funct'


def addition(num1,num2):
    result = num1+num2
    return result

def get_multiplication_table(num1,num=3):
    result = num1*num
    return result