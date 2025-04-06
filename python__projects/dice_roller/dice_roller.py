import random

min = 1
max = 6
roll_again = 'yes'


while roll_again == 'yes' or roll_again == 'y':
    
    
    number = int(input("How many dices : "))

    print("The  number(s) came to be : ")

    for x in range(number):
        computer_choice = random.randint(min,max)
       
        print(computer_choice)

    roll_again = input("want to roll again ?  (yes/y or no/n ) : ")  