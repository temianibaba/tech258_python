# Standard library

# Standard library consists of many modules and packages that are very useful, and were considered as default
#
# import random
#
# print(random.random())
# print(random.randrange(1, 10))

# import math
#
# num_float = 23.66
# print(math.ceil(num_float)) #roundup
# print(math.floor(num_float)) #round down
# print(math.pi)
# print(f"remainder from 1/5: {math.remainder(1,5)}")

# import os
#
# # returning current working directory
# working_dir = os.getcwd()
# print(f"Current working directory is:{working_dir}")
#
# # get user
# username = os.environ.get("USERNAME") or os.environ.get("USER")
# print(f"Username is: {username}")
#
# # cpu cores
# cpu_cores = os.cpu_count()
# print(f"Amount of CPUs: {cpu_cores}")
#
# # making/remove directory
# os.mkdir("test_dir")
# os.rmdir("test_dir")

import sys
# # sys demo
# # print(f"Current path: {sys.path}")
# print(sys.version)

# import datetime
#
# print(f"Today's date is: {datetime.datetime.today()}")
#
# import builtins
#
# for name in dir(builtins):
#     if name[0].islower():
#         print(name)


# import requests
#
# request_bbc = requests.get("https://www.bbc.co.uk/")
# print(request_bbc.status_code) #200--> Okay
# print(request_bbc.content)