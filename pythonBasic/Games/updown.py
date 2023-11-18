def runUpDown():
    import random
    answer = random.randrange(1, 10)
    chance = 7

    while chance > 0:
        user_input = int(input("값을 입력하세요 >>"))
        if user_input == answer:
            print("correct")
            break
        else:
            chance = chance - 1
            if user_input > answer:
                print("down")
            else:
                print("up")
    if chance == 0:
        print("game over")

