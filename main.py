age = int(input("How old are you?\n"))

death_age = 90
death_in_weeks = death_age * 52

age_in_weeks = age * 52

weeks_left = death_in_weeks - age_in_weeks

print(f"You are having {weeks_left} weeks left.")