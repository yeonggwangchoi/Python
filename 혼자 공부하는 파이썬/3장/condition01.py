num = input("정수 입력> ")

last_character = num[-1]

last_num = int(last_character)

if last_num == 0 or last_num == 2 or last_num == 4 or last_num == 6 or last_num == 8 :
    print("짝수입니다.")

if last_num == 1 or last_num == 3 or last_num == 5 or last_num == 7 or last_num == 9 :
    print("홀수입니다.")    