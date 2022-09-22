import random

def guessing_game():
    randnumber = random.randint(0,100)
    count = 0
    while True:

        if count == 3:
            print("문제를 맞추지 못했습니다.")
            break
        else:
            number = int(input("숫자를 맞춰보세요 >> "))
       
            if number > randnumber :
                print("Too high")
            elif number < randnumber:
                print("Too low")
            else:
                print("Just right")
                break

        count = count + 1
guessing_game()