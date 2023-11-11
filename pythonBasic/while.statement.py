# num = 0
#
#
# while num < 10:
#     print(num)
#     num += 1
#
# print("====메뉴====")
# print("1. 시작하기")
# print("2. 종료하기")
# print("==========")

# user_input = -1
#
# while user_input != 2:
#     user_input = int(input("값을 입력하세요 >>"))

# while True:
#     print("=====메뉴=====")
#     print("1. 시작하기")
#     print("2. 종료하기")
#     print("==============")
#
#     user_input = int(input("값을 입력하세요 >>"))
#     if user_input == 2:
#         break

# import random
# answer = random.randrange(0, 10)
# 사용자가 answer 맞출때까지 반복

# while True:
#     user_input = int(input("값을 입력하세요 >>"))
#     if user_input > answer:
#         print("down")
#     elif user_input < answer:
#         print("up")
#     elif user_input == answer:
#         print("정답입니다")
#         break
import random
answer = random.randrange(0, 10)
chance = 3

while chance > 0:
    user_input = int(input("값을 입력하세요 >>"))
    if user_input == answer:
        print("correct")
        break
    else:
        chance = chance -1
        if user_input > answer:
            print("down")
        else:
            print("up")
if chance == 0:
    print("game over")