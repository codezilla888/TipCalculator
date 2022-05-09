print("Welcome to the tip calculator.\n")
total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? "))
number_of_people = int(input("How many people to split the bill? "))
result = total_bill * (1 + percentage / 100) / number_of_people
rounded_result = "{:.2f}".format(result)
print(f"Each person should pay: ${rounded_result}")

