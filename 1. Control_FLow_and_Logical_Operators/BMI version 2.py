# Enter your height in meters e.g., 1.65
Your_height = float(input())

# Enter your weight in kilograms e.g., 65
Your_weight = float(input())


# Calculate your BMI by the function BMI = Weight / (Height ^ 2)

Your_BMI = round(Your_weight / (Your_height ** 2), 2)

# The interpretation of Your BMI 

if (Your_BMI < 18.5):
    print(f'Your BMI is {Your_BMI}, Your are Underweight')
    print(f'Since {Your_weight} / ({Your_height} x {Your_height}) = {Your_BMI}')
elif (Your_BMI < 25):
    print(f'Your BMI is {Your_BMI}, Your have a normal weight')
    print(f'Since {Your_weight} / ({Your_height} x {Your_height}) = {Your_BMI}')
elif (Your_BMI < 30):
    print(f'Your BMI is {Your_BMI}, Your are slightly overweight')
    print(f'Since {Your_weight} / ({Your_height} x {Your_height}) = {Your_BMI}')
elif (Your_BMI < 35):
    print(f'Your BMI is {Your_BMI}, Your are obese')
    print(f'Since {Your_weight} / ({Your_height} x {Your_height}) = {Your_BMI}')
else:
    print(f'Your BMI is {Your_BMI}, Your are clinically obese')
    print(f'Since {Your_weight} / ({Your_height} x {Your_height}) = {Your_BMI}')
    