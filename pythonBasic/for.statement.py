numbers = [1, 2, 3, 4]  #들여쓰기 조심하기
strings = ["hello","world"]

anys = [1,"hello",True,[1,2,3,4]]

print( numbers[0] )  #0번째 요소는 첫 번째 요소이다
print(strings[0])

print(anys[3][2])

scores = [84, 65, -5, -12, 79, 91, 50, 80, 54, 23, 58, 98, 64, 95, 90, 39, 84, 67, 82, 99, 91]
print(scores[3:])  #3번째 이전의 값
print(scores[1:4])  #1부터 4가지의 값
print(scores[:3])  #3번째 이후의 값


#평균을 구하고 싶을때
sum=0
for i in scores:
 if i > 100 or i < 0:
  print("skip!", i)
  continue
 sum = sum + i

average = sum / len(scores)
print("총합", sum)
print("평균 점수", average)

# for i in range(0,11):
#  print(i) ## ctrl + / 는 주석처리
