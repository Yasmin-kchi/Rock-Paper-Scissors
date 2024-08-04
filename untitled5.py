

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

choice = int(input("What o you choose? Type 0 for rock, 1 for paper or 2 for scissors\n"))
choices = [rock, paper, scissors]
x = choices[choice]
print(x)
rand_choice = random.randint(0, 2)
y = choices[rand_choice]
print("The computr choice is\n")
print(y)

if x == y:
    print("You are equal. Try again!")
if choice == 0 :
    if rand_choice == 1:
        print("You lose.")
    if rand_choice == 2:
        print("You win.")
elif choice == 1:
    if rand_choice == 0:
        print("You win.")
    if rand_choice == 2:
        print("You lose.")
elif choice == 2:
    if rand_choice == 0:
        print("You lose.")
    if rand_choice == 1:
        print("You win.")
        