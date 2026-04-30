try:
    marks=25
    result=25/0
    print(result)
except  ZeroDivisionError:
    print("a number cannot be divide by zero")
    
fruits = ["apple", "banana", "cherry"]

try:
    print(fruits[5])
except IndexError:
    print("Oops! That index doesn't exist.")

try:
    print(user_data) 
except NameError:
    print("Error: The variable 'user_data' is not defined.")
except TypeError:
    print("Error: You attempted an operation on an incorrect data type.")
finally:
    print("code runs succesfully")

try:
        f=open('myfile.txt', 'r') 
except FileNotFoundError:
    print("Oops! That file doesn't exist.")
finally:
    print("code is succesfull")

x=-7
if x<0:
    raise Exception ("sorry we cant accept below")

class ValueTooSmallError(Exception):
    """Raised when the input value is too small"""
    pass
class ValueTooLargeError(Exception):
    """raised when  the  input value is too large"""
    pass 





















