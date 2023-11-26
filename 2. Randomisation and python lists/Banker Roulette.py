# Who will pay the bill
import random as rd
# Enter the name of people who attend to this games e.g., Alex, Mice,...
Participants = input().split(", ")

Lucky_person_index = rd.randint(0, len(Participants))

print(f'{Participants[Lucky_person_index]} is going to buy the meal today!')

