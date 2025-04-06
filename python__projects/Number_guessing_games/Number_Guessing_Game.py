import random

print("First of all you have to input us the range between which the number will lie")
min = int(input("Enter the minimum number of the range : "))
max = int(input("Enter the maximum number of the range : "))

real_number = random.randint(min,max)
print(real_number)

guess = int(input("enter your try:  "))
number_of_guesses = 1
while real_number != guess :
    if real_number == guess:
        number_of_guesses = number_of_guesses+ 1
        break
    elif real_number > guess:
        print("the number you entered is too small")
        guess = int(input("enter your try again : "))
        number_of_guesses +=1

    elif real_number < guess:
        print("the number you entered is too large")   
        guess = int(input("enter your try again : "))
        number_of_guesses += 1
    else:
        print("invalid!")
        continue 
print("Congratulations you won!")
print(f"the number of tries were {number_of_guesses}")