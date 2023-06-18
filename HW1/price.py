from random import randint


a = randint(0, 1001)
k = 9
while True:
    b = int(input("Try to guess: "))
    if a == b:
        print("You are awesome")
        break
    elif k == 0:
        print("You lost")
        break
    elif a > b:
        print("There is few, try again")
    else:
        print("There is much, try again")
    k -= 1
