# Functions

# DRY - DON'T REPEAT YOURSELF

# no argument
# def print_something():
#     print("something has been printed")
#
# def print_something2(name):
#     print("Hello, my name is " + name)
#
# print_something2("Temi")

# Argument
# def addition(int1, int2):
#     return int1 + int2
#
#
# print(addition(2, 2))

# default argument can be overwritten
# def addition(int1=2, int2=2):
#     return int1 + int2
#
# print(addition())
# print(addition(10, 15))
#
# # multiple arguments
# def multi_argus(*MCU):
#     for arg in multi_argus:
#         print(arg)
#
# multi_argus(1, 2, 3, 4, 5)