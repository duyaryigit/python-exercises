
# Python program for calculating body mass index according to the height and weight values entered by the user.

height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight / (height/100)**2

print(f"You BMI is {BMI}")

if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are over weight.")
elif BMI <= 34.9:
    print("You are severely over weight.")
elif BMI <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")

'''
Output Example:

Enter your height in cm: 177
Enter your weight in kg: 91
You BMI is 29.046570270356536
You are over weight.

'''