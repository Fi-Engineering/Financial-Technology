a = 5                        # sample code only to demonstrate how to print
print("Test value:",a)       # Copy this line and modify the label and variable
                             # to display results
                             
                             
hours = float(input('How many hours did the employee work? '))
rate =  float(input('What is the employee\'s pay rate? '))
if(hours<=40):
    grossPay = hours * rate
else:
    grossPay = 40 * rate + (hours - 40) *(rate * 1.5)
taxDue = grossPay * 0.20
netPay = grossPay - taxDue
print('Total pay: ', grossPay)
print('Taxes: ', taxDue)
print('Net pay: ', netPay)

                         
                            