# 2. Sales Prediction
# A company has determined that its annual profit is typically 23 percent of total sales. Write
# a program that asks the user to enter the projected amount of total sales, then displays the
# profit that will be made from that amount.
# Hint: Use the value 0.23 to represent 23 percent.

# thse company total amount of sales entered by the UserWarning

companyTotalSales = float( input('enter the total projected of company\'s sales $'.title()).strip().title() )

# calculating the company profit => profit percntage = 23 % == 0.23

companyProfit = 0.23 # the profit in percentage
totalCompanyProfit = companyTotalSales * companyProfit

print(f' from ${companyTotalSales} the company earn a profit of ${totalCompanyProfit}'.title())

