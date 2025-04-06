from random import choice

choices = ['rock','paper','scissor']

user_score = 0

computer_score = 0


for x in range(10):
   
    print(f"\nRound {1+x}")
    user_choice = input("enter rock/paper/scissor : ").lower()
    if user_choice not in choices:
        print("Enter valid choice")
        continue
    computer_choice = choice(choices)

    if (user_choice=='rock' and computer_choice =='scissor') or \
          (user_choice == 'paper' and computer_choice == 'rock') or \
          user_choice == 'scissor'  and computer_choice == 'paper' :
        print(f"your choice : {user_choice}")
        print(f"computer choice : {computer_choice}")
        print("you win")
        user_score += 1
        print(f"your score : {user_score } || computer score: {computer_score}")
    elif(user_choice == 'rock' and computer_choice == 'rock') or \
    (user_choice == 'paper' and computer_choice == 'paper') or \
    (user_choice == 'scissor' and computer_choice == 'paper'):
        print(f"your choice : {user_choice}")
        print(f"computer choice : {computer_choice}")
        print("drawn")
        print(f"your score :{user_score } || computer score:{computer_score}")
    else:
         print(f"your choice : {user_choice}")
         print(f"computer choice : {computer_choice}")
         print("You lose")
         computer_score +=1
         print(f"your score :{user_score } || computer score:{computer_score }")
         
print("game is completed")

print(f"your final score : {user_score}")

print(f"computer's final score: {computer_score}")

if(user_score>computer_score):
    print("you are the champion \n", end = '\n' )
elif(user_score==computer_score):
    print("the game is drawn\n" ,end = '\n')
else:
    print("computer defeated you\n", end = '\n')

'''
concepts used:
1. Conditionals
2. For loops
3. Lists
4. Functions(as used to import random module)
5. Rules of rock,paper,scissor
'''