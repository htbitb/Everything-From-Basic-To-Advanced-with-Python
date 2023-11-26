""" Interview Question
There are the rules of the FizzBuzz Game:
    * Your program should print each number from 1 to 100
    * When the number is divisible by 3 -> print "Fizz"
    * when the number is divisible by 5 -> print "Buzz"
    * If number is divisible both 3 and 5 -> print "FizzBuzz"
"""

for number in range (1, 100 + 1):
    if (number % 3 == 0 and number % 5 == 0):
        print("FizzBuzz")
    elif (number % 3 == 0):
        print("Fizz")
    elif (number % 5  == 0):
        print("Buzz")
    else:
        print(number)