import random

def guessing_game():
    randnumber = random.randint(0,100)
    number = -1
    while number!=randnumber:
        number = int(input("숫자를 맞춰보세요 >> "))
       
        if number > randnumber :
            print("Too high")
        elif number < randnumber:
            print("Too low")
        else:
            print("Just right")

guessing_game()





