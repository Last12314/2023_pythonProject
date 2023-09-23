# f(x) = 3x + 5
def tmpFunction(x):
    return x * 3 + 5

print(tmpFunction(5))

#개임 예시
#화면 뿌려주기 <- 기늠
#랜덤 값 할당 받기<- 기능
#사용자 값 입력받기 <- 기능
#값이랑 사용자 값 비교하기 <- 기능

def menuPrint():
    print("======GAME======")
    print("1. 행맨")
    print("2. 업다운")
    print("3. 종료")
    print("================")
def GetRandomWord():
    import random
    words = ["hang", "apple", "ant", "samsung", "MCdonalds", "fluent", "voca", "galaxy"]
    return words[random.randrange(0, len(words))]

def getHangmanInput():
    while True:
        user_input = input("Input alphabet ::: ")
        if(user_input.isapha()):
            alphabet = user_input[0].lower
            if(hangman_input_history.index(alphabet)):
                print("이미 입력한 값이다. 다른 값을 입력해라.")
            else:
                return alphabet

hangman_input_history = []      #전역변수, 지역변수
                                #전역변수는 띄어쓰기 없이 사용되며 모든 코드에서 사용될 수 있다
                                #지역변수는 if문이나 함수 안에 들어가 있는 변수
                                #if문이나 함수 안에서만 사용되고 그 함수가 끝나면 변수는 소멸된다
                                #또한 전역변수와 지역변수는 이름이 같지 않아야 한다

def runHangMan():
    hangman_input_history = []
    word = GetRandomWord()
    print("_"*len(word))

    alphabet = getHangmanInput(hangman_input_history)



def runUpDown():
    import random
    answer = random.randrange(1, 10)
    chance = 3

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


userInput = -1

while userInput != 3:
    menuPrint()
    userInput = int(input("SELECT MENU :::"))

    if userInput == 1:
        runHangMan()
    elif userInput ==2:
        runUpDown()