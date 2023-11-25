import pygame
import random



# 색상 dictionary
colors = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    '-1': (200, 200, 200),
    '2': (224, 247, 250),
    '4': (178, 235, 242),
    '8': (128, 222, 234),
    '16': (77, 208, 225),
    '32': (38, 198, 218),
    '64': (0, 188, 212),
    '128': (0, 172, 193),
    '256': (0, 151, 167),
    '512': (0, 131, 143),
    '1024': (0, 96, 100),
    '2048': (0, 0, 0),
}


# 실제 게임 로직이 반영될 보드
board = [[-1, -1, -1, -1],
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
        [-1, -1, -1, -1]]


# 화면 관련 설정
size = (500, 500)
screen = pygame.display.set_mode(size)


def initScreen():
    screen.fill(colors['white'])
    pygame.display.update()


def addNewBlock():
    canSet = False
    while not canSet:
        randomX = random.randint(0, 3)
        randomY = random.randint(0, 3)

        if board[randomX][randomY] == -1:
            canSet = True


    board[randomX][randomY] = 2 if random.randint(1,10) < 10 else 4  #10분의 1의 확률로 4, 이외에는 2가 추가되도록.


# 게임 진행 flag 변수
isGameRunning = True

def setEventListener():
    global isGameRunning
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                isGameRunning = False
                return

            elif event == pygame.K_DOWN:
                print("아래")
            elif event == pygame.K_UP:
                print("위")
            elif event == pygame.K_RIGHT:
                print("오른쪽")
            elif event == pygame.K_LEFT:
                print("왼쪽")

            addNewBlock()

def drawDisplay():
    baseX = 35
    baseY = 35
    blockHeight = 100
    blockWidth = 100
    margin = 10

    for i in range(4):
        for j in range(4):
            x = (blockWidth + margin) * j + baseX
            y = (blockHeight + margin) * i + baseY
            data = str(board[i][j])
            if data == '-1':  ##데이터가 없을때
                pygame.draw.rect(screen, colors[data], [x, y, blockWidth, blockHeight], 2)  # outlined rect
            else :
                pygame.draw.rect(screen, colors[data], [x, y, blockWidth, blockHeight])   # filled rect
    pygame.display.flip()




def run2048():
    pygame.init()
    initScreen()
    print("2048 게임 시작")

    while isGameRunning:
        setEventListener()
        drawDisplay()


    pygame.quit()

run2048()


'''
#### #### #### ####
#### #### #### ####
#### #### #### ####
#### #### #### ####

0008 0016 #### ####
0008 0004 0004 0008
0512 0128 0064 0008
2048 1024 0512 0128

1. 화면출력 모두 ####이고, 2와 4가 랜덤 위치에 뜨게
#### #### 0004 ####
#### 0002 #### ####
#### #### #### ####
#### #### #### ####

2. 사용자의 움직임이 있으면 그 방향으로 숫자를 밀고 빈칸 중 하나(랜덤위치)에 2, 4 중에서 하나가 뜨게
3. 블럭이 한방향으로 모일때 해당 방향에 같은 숫자가 있으면 블럭 합치기

(아랫방향 입력시)
#### #### #### ####
#### #### 0002 ####
#### #### #### ####
#### 0002 0004 ####

(왼쪽방향 입력시)
#### #### #### ####
0002 #### 0002 ####
#### #### #### ####
0002 0004 #### ####

(아랫방향 입력시)
#### #### #### ####
0002 #### #### ####
#### #### #### ####
0004 0004 #### ####


4. 최종적으로 2048이 만들어졌으면 WIN.
'''

# i = 4
# j = 4
#
# data = [[0]*i for k in range(j)]
#
# n=0
# sw=1
# end = len(data[0]) -1
# start=0
#
# for i in range(len(data)):
#     for j in range(start,end+sw,sw):
#         n+=1
#         data[i][j] += n
#     start, end = end, start
#     sw = sw* -1
#
# for i in range(len(data)):
#     for j in range(len(data[0])):
#         print("%2d" % data[i][j],end = ' ')
#     print()

# data =[["####", "####", "####", "####"], ["####", "####", "####", "####"], ["####", "####", "####", "####"], ["####", "####", "####", "####"]]
# for i in range(4):
#     print(data[0], data[1], data[2], data[3])
#     print()
