p = float(input("What is the amount borrowed? "))

r = float(input("nWhat is the annual interest rate - express this as a decimal such as 0.07 for 7%? "))

y = 30
m = 12

n = y * m  # periods per year * number of years:
r = r / m

A = p*(r * (1 + r)**n) / ((1+ r)**n -1)

payment_amount = int(A*100)/100 #converts answer to whole cents (int)
print(payment_amount)