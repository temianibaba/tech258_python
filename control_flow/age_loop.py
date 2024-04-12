user_prompt = True

while user_prompt is True:
    age = input("What is your age? ")
    if age.isdigit() and int(age) < 118 :
        # SET user_prompt TO FALSE
        user_prompt = False

    else:
        # TELL USER THE PROBLEM WITH THEIR INPUT
        print("PUT A real or smaller NUMBER IN!!!")


print(f"Your age is {age}")