# Day 2 Tip Calculator
# Author: Damian Wetzel

# Get user input
print("Welcome to the tip calculator.")
bill_subtotal = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_of_ppl = int(input("How many people to split the bill? "))

# Calculations
tip_amount = bill_subtotal * (tip_percentage / 100)
total_bill = bill_subtotal + tip_amount
individual_amount = round(total_bill / num_of_ppl, 2)

# Print Result
print(f"Each person should pay: ${individual_amount}")
