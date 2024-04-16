print("Welcome to the tip calculator.\n")
total = float(input("What was the total bill?\n$"))
percentage = int(input("What percentage tip would you like to give?\n10, 12 or 15?\n"))
people = int(input("How many people to split the bill?\n"))

proportion = "{:.2f}".format(total * (1 + percentage / 100) / people)

print(f"Each person should pay: ${proportion}")