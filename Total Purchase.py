# problem 4

# 4. Total Purchase
# A customer in a store is purchasing five items. Write a program that asks for the price of
# each item, then displays the subtotal of the sale, the amount of sales tax, and the total.
# Assume the sales tax is 7 percent.


# the price for the five items entered by the user
item1_price = float( input('enter the price for item 1 $'.title() ).strip() )
item2_price = float( input('enter the price for item 2 $'.title() ).strip() )
item3_price = float( input('enter the price for item 3 $'.title() ).strip() )
item4_price = float( input('enter the price for item 4 $'.title() ).strip() )
item5_price = float( input('enter the price for item 5 $'.title() ).strip() )

# calculating the subTotl of all items 
subtotal = item1_price + item2_price + item3_price + item4_price + item5_price

# caculating the tax for all items entered by the User 
tax_percentage = 0.07
totalTax = subtotal * tax_percentage

# calculating the total
total_bill = subtotal + totalTax

print(f'\n\nthe item 1 price is \"${item1_price:.2f}\"\nthe item 2 price is \"${item2_price:.2f}\"\nthe item 3 \
      price is \"${item3_price:.2f}\"\nthe item 4 price it \"${item4_price:.2f}\"\nthe item 5 price is $\" \
      {item5_price:.2f}\"\nthe amount of subtotal is \"{subtotal:.2f}\"\nthe amount of tax for all items is \" \
      {totalTax:.2f}\"\nthe total bill is \"{total_bill:.2f}\""'.title())
