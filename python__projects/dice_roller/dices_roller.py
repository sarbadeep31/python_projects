import random

min = 1
max = 6
roll_again = 'yes'

number_of_dices = int(input("How many dices : "))

while roll_again == 'yes' or roll_again == 'y':
    
    
    

    print("The  number(s) came to be : ")

    for x in range(number_of_dices):
        computer_choice = random.randint(min,max)
       
        print(computer_choice)

    roll_again = input("want to roll again ?  (yes/y or no/n ) : ")  