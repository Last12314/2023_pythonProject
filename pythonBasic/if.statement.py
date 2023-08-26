score = float(input("이번 외국어 영역의 백분위를 숫자만 입력해 주세요, ex) 2.4\n"))

# if score > 90 and score <=100:
#      print("A grade")
#
# if score > 80 and score <= 90:
#     print("B grade")
#
# if score > 70 and score <= 80:
#     print("C grade")
#
# if score > 60 and score <= 70:
#     print("D grade")
#
# if score >=\ 50 and score <= 60:
#     print("E grade")



if score > 90 and score <=100:
     print("A grade")

elif score >= 80:
    print("B grade")

elif score >= 70:
    print("C grade")

elif score >= 60:
    print("D grade")

elif score >= 0 and score <60:
    print("E grade")

else:  #여기서 '콜론'은 이 코드 다음에 동작을 수행하라는 역할
    print("값이 잘못됨")
    print("다시 해라...")