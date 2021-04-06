import random

# import sys
from time import sleep



def game(i):

    n = ["s", "r", "p"]
    c = random.choice(n)

    if c == i:
        print("Computer entered- " + c)
        return print("It's a TIE!!!")
    elif c == "r" and i == "p":
        print("Computer entered- " + c)
        return print("You Won")
    elif c == "p" and i == "s":
        print("Computer entered- " + c)
        return print("You Won")
    elif c == "s" and i == "r":
        print("Computer entered- " + c)
        return print("You Won")
    else:
        print("Computer entered- " + c)
        return print("You Lost!!!")


while True:
    a = input("Enter s, p, or r- ")
    if a == "s" or a == "p" or a == "r":
        game(a)

    else:
        print("!!!INVALID INPUT!!!")

    Q = input("Press any key to continue and 'q' to Quit- ")

    if Q == "q":
        print("Thanks for playing this game")
        sleep(2)
        exit()

# if (a!= "s" or a!= "p" or a!= "r"):
#     print("!!!INVALID INPUT!!!")
# else:
#     print("Computer entered- "+c)
#     game(c,a)
