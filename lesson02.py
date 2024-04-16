height = float(input("How tall are you (in meters)?\n"))
weight = float(input("How much do you weight (in kilogram)?\n"))

bmi = int(weight / height ** 2)

print("Your BMI is " + str(bmi) + ".")