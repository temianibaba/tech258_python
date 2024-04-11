# Strings
# Can use single or double quotes ' ' or " "
# Use " " because some words use '

# String Slicing
# Hw = "Hello World!"
#
# # How many characters
# print(len(Hw))
# # Target first Char
# print(Hw[0])
# # Target last char
# print(Hw[-1])
# # Use negative indexing to get second to last
# print(Hw[-2])
# # use string slicing to get the first 3 characters
# print(Hw[:3])

# String methods
# Strip removes spaces after string
# Count substring - var.count("text")
# Lowercase Uppercase .lower() .upper()
# Capitalised .capitalize()
# Replace .replace("text", "replacement")

# Adding strings is concatenation

# x = 2
# y = 5.4
# z = " there's now a number 25.4 unless we put a space in"
# print(str(x) + " " + str(y) + z)

# F-strings

# name = "Lassie"
# years = 7
# height_cm = 183
#
# print(f"{name} is {years} years old and {height_cm} cm tall")

# pi = 3.14159265359
# print(f"{pi:.5f}")
# print(f"{pi:.3f}")

score = 50
max_score = 100

print(f"You scored {score/max_score}")
print(f"You scored {score/max_score:%}")