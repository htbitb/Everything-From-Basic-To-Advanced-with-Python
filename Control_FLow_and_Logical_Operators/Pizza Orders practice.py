"""
You are requested to build a automatic pizza order base on customer's choice

------
Small pizza (S): $15
Medium pizza (M): $20
Large pizza (L): $25
------
Add pepperoni for small pizza (Y or N): +$2
Add pepperoni for Medium or Large (Y or N): +$3
------
Add extra cheese for any size (Y or N): +$1
"""

print('Thank you for choosing htb pizza Deliveries \nPlease choose which you want')

print('Size of pizza (S for small - M for Medium - L for Large): ')
Size = input()

print('Do you want to add pepperoni for it (Y or N): ')
add_pepperoni = input()

print ('Do you want to add extra cheese (Y or N):')
extra_cheese = input()

# calculate the bill
Total_bill = 0

if (Size == 'S'):
    Total_bill += 15
    if(add_pepperoni == 'Y'):
        Total_bill += 2
elif (Size == 'M'):
    Total_bill += 20
    if(add_pepperoni == 'Y'):
        Total_bill += 3     
else:
    Total_bill += 25
    if(add_pepperoni == 'Y'):
        Total_bill += 3

if (extra_cheese == 'Y'):
    Total_bill += 1

print(f'Your total bill is ${Total_bill} \nThanks for your order')