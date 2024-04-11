# Let's help with generating a bill with tips added and allow the user to split among a number of people

# Get the bill from the user

initial_bill = float(input("What is your total bill tonight? "))

# Calculate the tip (assume a percentage of 10-15%)
tip = initial_bill * 0.15

# Calculate bill with the tip added
total_bill = initial_bill + tip

# Ask how many people they want to split with

participants = int(input("How many people are paying? "))

# Calculate the bill divided by the split amount
indi_bill = total_bill / participants

# Print the split bill per person, being rounded to 2 decimal places - you will have to research how to display to 2 decimal places
print(f"Bill per person: {indi_bill:.2f}")