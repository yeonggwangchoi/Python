import time

number = 0

target_tick = time.time() + 5
while time.time() < target_tick:
    number += 1
    
print("5초 동안 %d번 반복했습니다.",number)