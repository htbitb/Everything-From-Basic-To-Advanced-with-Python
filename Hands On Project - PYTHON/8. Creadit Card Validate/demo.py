card_no = "56105591081018250"
double_list = []
odd_num = 0

number = list(card_no)
sum = 0
for key,val in enumerate(number):
    if key % 2 != 0:
        sum += int(val)
    else:
        double_list.append(int(val) * 2)
print(double_list)

#converting the list into a string

double_str = ""
for x in double_list:
    double_str += str(x)