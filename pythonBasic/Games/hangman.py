def GetRandomWord():
    import random
    words = ["hang", "apple", "ant", "samsung", "mcdonalds", "float", "voca", "galaxy"]
    return words[random.randrange(0, len(words))]

def getHangmanInput():
    while True:
        user_input = input("Input alphabet ::: ")
        if(user_input.isalpha()):  #알파벳인지 확인
            alphabet = user_input[0].lower()
            if(alphabet in hangman_input_history): #이미 입력한 값 인지
                print("이미 입력한 값이다. 다른 값을 입력해라.")
            else:
                return alphabet

# 전역변수, 지역변수
# 전역변수는 띄어쓰기 없이 사용되며 파이썬 전체에서 사용될 수 있다
# 지역변수는 특정 구문이나 함수 안에 들어가 있는 변수
# 구문이나 함수 안에서만 사용되고 그 함수가 끝나면 변수는 소멸된다
# 또한 전역변수와 지역변수는 이름이 같지 않아야 한다

def printPresentWords(word):
    printStr = ""
    for i in word:
        if i in hangman_input_history:
            printStr = printStr + i
        else:
            printStr = printStr + "_"
        printStr = printStr + " "

    print(printStr)

def runHangMan():
    global hangman_input_history

    # 초기화용 코드
    hangman_input_history = []
    chance = 7
    correct = 0

    word = GetRandomWord()
    wordSet = set(word)

    while chance > 0:

        printPresentWords(word)

        alphabet = str(getHangmanInput())

        hangman_input_history.append(alphabet)

        if word.find(alphabet) != -1:  # alphabet이 word에 속해있으면 정답이라고 알려주고, 아니면 기회를 깎기.
            correct = correct +1
            print("CORRECT!")
        else:
            chance = chance - 1

            if chance == 0:
                print("You Die")
            else:
                print("LEFT CHANCE : ", chance)


        if correct >= len(wordSet): # 정답을 맞췄을때 게임 종료
            print("Alive!")
            break






    #알파벳이 워드에 속해있으면 정답이라고 알려주고, 아니면 기회를 깍기
    #기회가 8이상 틀렷을때는 게임 아웃
    #화면에 남은 횟수 보여주기