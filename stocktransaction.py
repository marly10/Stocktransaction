#Homework 3 details

#You decide to buy some stocks for a certain price.
#then sell them at another price. 
# Write a program that determines whether or not 
# the transaction was profitable.

#Input of shares, price bought and sales data

#Only takes whole number with no decimals(INT)
shares = int(input('Enter number of shares:'))

#Both take whole and fraction/decimals number as Inputs (FLOAT)
purchase_price = float(input('Enter purchase price:'))
sale_price = float(input('Enter sale price:'))

#The total price for shares bought
cost=float(shares*purchase_price)

#Pay your stockbroker a commission of 3 percent on the amount paid for the stock
commission=float(cost*.03)

#Total amount pay for stock with .03 commission included
total=float(cost+commission)

#The total payment for the sales of stock at a Inputed price
sale_total=float(shares*sale_price)

# Pay your stockbroker another commission of 3 percent on the amount you received for the stock.
commission_2=float(sale_total*.03)

#total income after commission is paid and all stock is sold
income=float(sale_total-commission_2)
profit=float(income-total)

#if statement where if the profit is greater will print. Money gained!!
if (profit>=int(0)):(print('After the transaction , you made ' + format(profit) + ' dollars.' + 'Good Job!!'))

#if statement where if the profit is less will print. Money lost!!
else:(print('After the transaction, you lost ' + format(profit*-1) + ' dollars.' ))

#Data output/Print for total paid for stock.
print("The Total I paid for Stocks:", end=" ")
print(format(total))

#Data output/Print for total amount the stock sold for.
print("The Total I sold the Stocks:", end=" ")
print(format(income))

#Data output/Print for stock purchase
print("Total Commission(.03) paid for Stock Purchase:", end=" ")
print(format(commission))

#Data output/Print for stock sold
print("Total Commission(.03) paid for Stock sale:", end=" ")
print(format(commission_2))


#Meaning of float and inputs
#float(): Outputs number with decimals 10.1
#int(): In this context outputs numbers without decimal 10
