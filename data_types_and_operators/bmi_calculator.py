# Get the user's height and weight
print("Welcome to your BMI calculator please type your height in m and weight in kg when prompted.")

height = float(input("Height in m? "))


weight = int(input("Weight in kg? "))

# Calculate their BMI from the height and weight given
heightsqr = height * height
bmi = weight / heightsqr

# Print the BMI as a message to the user
print(f"Your bmi is : {bmi:.1f}")
