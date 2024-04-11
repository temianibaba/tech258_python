# Defining starter mains dessert

# level 1
# Greet the user
print("Hello! It's nice to see you, here are the starters for today.")
# Print a list of starters
starters = ["Spring Rolls", "Haloumi Fries", "Chicken Skewers"]
print(starters)
# Take an input for the user for their starter
cs_starter = input("What would you like for your starter?")
# Print a list of mains
mains = ["8 oz Steak with seasoned chips", "Buttercream Chicken", "Salmon", "Veg salad"]
print(mains)
# Take an input for the user for their main course
cs_mains = input("What would you like for your main?")
# Print a list of desserts
desserts = ["Chocolate cake", "Apple scrumble", "Ice cream"]
print(desserts)
# Take an input for the user for their dessert
cs_desserts = input("What would you like for dessert?")
# Print all of the user's choices
cs_order = [cs_starter, cs_mains, cs_desserts]
print("You ordered:", cs_order)
# level 2
# Use at least one f-string
# Add each item ordered to a list called 'customer_order_list'
print(f"For your starter you had {cs_starter}")
print(f"For your main you had {cs_mains}")
print(f"For your dessert you had {cs_desserts}")
print("You ordered:", cs_order)
# level 3
# Use dictionaries and assign prices to the items. Create a bill at the end of the program.
pricing = {
    "starters": {
        "Spring rolls": 2.99,
        "Haloumi Fries": 1.99,
        "Chicken Skewers": 3.49,
    },
    "mains": {
        "8 oz Steak with seasoned chips": 12.99,
        "Buttercream Chicken": 11.99,
        "Salmon": 11.99,
    },
    "desserts": {
        "Chocolate cake": 5.99,
        "Apple scrumble": 4.99,
        "Ice cream": 3.99,
    }
}
user_starter_price = float(pricing["starters"][cs_starter])
print(user_starter_price)
user_main_price = float(pricing["mains"][cs_mains])
print(user_main_price)
user_dessert_price = float(pricing["desserts"][cs_desserts])
print(user_dessert_price)
total_bill = user_starter_price + user_main_price + user_dessert_price
print(f"Total bill £{total_bill}")