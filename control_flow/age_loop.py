user_prompt = True

while user_prompt is True:
    age = input("What is your age? ")
    if age.isdigit() and int(age) < 118 :
        user_prompt = False

    else:
        print("PUT A real or smaller NUMBER IN!!!")

# SET user_prompt TO FALSE
# ADD ELSE STATEMENT HERE
# TELL USER THE PROBLEM WITH THEIR INPUT

print(f"Your age is {age}")