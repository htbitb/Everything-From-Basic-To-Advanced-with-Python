# Init value rock paper scissor
import random as rd
win = 0
lose = 0
# Rock
Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
# Paper
Paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# SCissors
Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# You have three rounds to play, if you won 2 out of 3, you win and vice versa
def Shape_of_choosing(index):
    if (index == 0):
        print(Rock)
    elif (index == 1):
        print(Paper)
    else:
        print(Scissors)

for rounds in range(0,3):
    print(f'Rounds {rounds} - which is your choice? (0 for Rock/ 1 for Paper/ 2 for Scissors):')
    
    Your_choice = int(input())
    print('You choice', end= ' ')
    Shape_of_choosing(Your_choice)
    
    computer_choice = rd.randint(0, 2)
    print('Computer choice', end=' ')
    Shape_of_choosing(computer_choice)

    if (Your_choice < computer_choice):
        if (Your_choice == 0 and computer_choice == 2):
            print('You Win!')
            win += 1
        else:
            print('You lose!')
            lose += 1
    elif (Your_choice > computer_choice):
        if (Your_choice == 2 and computer_choice == 0):
            print('You Lose!')
            lose += 1
        else:
            print('You Win!')
            win += 1
    else:
        print('Draw!')
print(win , lose)
if (win > lose):
    print('Congratulation! You win computer')
elif (win < lose):
    print('Regret! you lose computer')
else:
    print('Draw')
        