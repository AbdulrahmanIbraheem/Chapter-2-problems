# 6. Payment Instalments
# Write a program that asks the user to enter the amount of a purchase and the desired
# number of payment instalments. The program should add 5 percent to the amount to get
# the total purchase amount, and then divide it by the desired number of instalments, then 
# display messages telling the user the total amount of the purchase and how much each
# instalment will cost.



# this will ask the user to enter the amount of purchase
amount_puchase = float( input('enter the amount of puchase please $'.title() ).strip() )

# here will ask the customer to enter the number of intersed instalments
number_of_instalments = int( input('enter the number of intersed instalments please '.title() ).title() )

# add 5 percentage to the amount purchase
add_5_percentage_to = amount_puchase * 0.05

# calculating the total_amount_purchase
total_purchase = amount_puchase + add_5_percentage_to

# caculating how much each instalments need to pay
payment = total_purchase / number_of_instalments

# display the output
print(f' \"${total_purchase:.2f}\" is the total amount purchase, each payent need to pay \"${payment:.2f}\" ')
