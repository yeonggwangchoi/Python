num = input("정수 입력> ")
last_charater = num[-1]

if last_charater in "02468" :
    print("짝수입니다")
    
if last_charater in "13579" :
    print("홀수입니다")

