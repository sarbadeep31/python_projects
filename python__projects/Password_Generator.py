import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRlawidjcLJHEBSTUVWXYZ1234567890!@#$%^&*()?><:;}{]"

user = int(input("enter length : "))

for x in range(user):
     password+=(random.choice(chars))
print(password)    