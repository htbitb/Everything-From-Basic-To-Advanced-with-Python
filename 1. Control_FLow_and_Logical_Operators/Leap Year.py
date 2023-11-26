# which year do you want to check?
year = int(input())

"""
Normal year has 365 days but Leap year has  366, with an extra day in February
This is how you work out:
    * Year is divided by 4 with no remainder
    * EXCEPT every year that is evenly divisible by 100 with no remainder
    * UNLESS the year is also divisible by 400 with no remainder
"""
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print(f'{year} is a Leap Year')
        else:
            print(f'{year} is not a leap year')
    else:
        print(f'{year} is not a leap year')
else:
    print(f'{year} is not a leap year')
            
            

    