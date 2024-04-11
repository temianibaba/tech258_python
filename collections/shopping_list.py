shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]
print(shopping_list)
print(type(shopping_list))
print(shopping_list[0])
print(shopping_list[-1])
shopping_list[1] = "rice"
print(shopping_list)
shopping_list.append("carrots")
print(len(shopping_list))
second_list = ["toffee", "coffee"]
# shopping_list.extend(second_list)
shopping_list = shopping_list + second_list
print(shopping_list)
shopping_list.pop(2) #shopping_list.remove("bananas")
print(shopping_list)
shopping_list.pop()
print(shopping_list)
shopping_list.append("tea")
print(shopping_list)
shopping_list.pop()
print(shopping_list)
