print("Welcome to the tip calculator!\n")
total_bill = float(input("What ws the total bill? $ "))
tip_percentage = int(input("How much tip would you like to give? "))
people_amount = int(input("How many people to split the bill? "))

final_tip_amount = (tip_percentage / 100 * total_bill + total_bill)

total_amount = (round(final_tip_amount / people_amount, 2))

print(f"Each person should pay: ${total_amount}")
