# 8. Tip, Tax, and Total
# Write a program that calculates the total amount of a meal purchased at a restaurant. The
# program should ask the user to enter the charge for the food, then calculate the amounts
# of a 18 percent tip and 7 percent sales tax. Display each of these amounts and the total.




tip = 0.18 # this is the tip in perentagee
tax = 0.07 # this is the tax in perventage

# the amount of  food charge . entered by the User
meal_charge = float( input('enter the price of the meal $'.title()).strip() )

total_tip = meal_charge * tip # this is the amount of tip will include
totalTax = meal_charge * tax  # this is the amount of tax will include

total = meal_charge + total_tip + totalTax # this to calculate the total for th meal 

print(f'\ntotal tax is ${totalTax:.2f}\ntotal tip is ${total_tip}\ntotal meal charge is ${total}'.title())
