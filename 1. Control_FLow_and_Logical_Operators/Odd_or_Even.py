# Which number do you want to check?
input_number = int(input())

# Using '%' and if else condition to check the type of number
#if the number can be divided by 2 with 0 remainder than it is even number.
 
if (input_number % 2 == 0):
    print(f'{input_number} is even number')
else:
    print(f'{input_number} is odd number')