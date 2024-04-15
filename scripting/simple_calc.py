# Simple calc functions
#import math_ops
# from math_ops import *
from math_ops import add, subtract, divide, multiply

operation = input("Pick one: add, subtract, divide, multiply \n")
user_input = True
while user_input == True:
    if operation == "add":
        user_input = False
        first_num = int(input("Enter the first number: "))
        second_num = int(input("Enter the second number: "))
        result = add(first_num, second_num)
        print(f"{first_num} + {second_num} = {result}")
    elif operation == "subtract":
        user_input = False
        first_num = int(input("Enter the first number: "))
        second_num = int(input("Enter the second number: "))
        result = subtract(first_num, second_num)
        print(f"{first_num} - {second_num} = {result}")
    elif operation == "divide":
        user_input = False
        first_num = int(input("Enter the first number: "))
        second_num = int(input("Enter the second number: "))
        result = divide(first_num, second_num)
        print(f"{first_num} / {second_num} = {result}")
    elif operation == "multiply":
        user_input = False
        first_num = int(input("Enter the first number: "))
        second_num = int(input("Enter the second number: "))
        result = multiply(first_num, second_num)
        print(f"{first_num} x {second_num} = {result}")
    else:
        user_input = True
        print("Please choose one of the given options.")
        operation = input("Pick one: add, subtract, divide, multiply \n")
