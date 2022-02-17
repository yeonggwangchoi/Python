print("숫자게임 시작합니다.")
number = 62

num = input("1에서 100사이의 숫자를 추측 해보세요.")
print(num)

#문자열로 넘어온 값은 int()를 이용하여 숫자로 바꿔주고 있다.
guess = int(num)

if guess == number :
    print("맞았습니다.")
else :
    print("틀렸습니다.")
    
print("게임을 종료합니다.")