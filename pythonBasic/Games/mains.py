from pythonBasic.Games.updown import runUpDown
from pythonBasic.Games.game2048 import run2048
from pythonBasic.Games.hangman import runHangMan


def menuPrint():
    print("======GAME======")
    print("1. 행맨")
    print("2. 업다운")
    print("3. 2048")
    print("4. 종료")
    print("================")

userInput = -1

while userInput != 4:
    menuPrint()
    userInput = int(input("SELECT MENU :::"))

    if userInput == 1:
        runHangMan()
    elif userInput ==2:
        runUpDown()
    elif userInput == 3:
        run2048()