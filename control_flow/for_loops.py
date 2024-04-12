list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1,2,3],[4,5,6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

# for numb in list_data:
#     print(numb)
#     print(numb)
#
# for ince in embedded_lists:
#     print(ince)
#     print(ince[0])
#     print(ince[1])
#     print(ince[2])
#
# for key in dict_data:
#     print(key)
#
# for value in dict_data:
#     print(dict_data.values())
#
# for value in dict_data.values():
#     print(value.get("money"))

for number in list_data:
    if number < 3 :
        print("Less than 3")
    elif number == 3:
        print("I found 3")
    else :
        print("Greater than 3")
