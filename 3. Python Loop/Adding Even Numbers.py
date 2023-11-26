"""_summary_
You are going to write a program that calculates the sum of all the even numbers from 1 to X.
"""

Target_number = int(input()) # Enter number between 0 and 100

even_sum = 0

for number in range (2, Target_number + 1, 2):
    even_sum += number

print(even_sum)

