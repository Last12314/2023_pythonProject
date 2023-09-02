# c = int(input("값을 입력해라\n"))
# for a in range(1,c):
#     b="*"*a
#     print(b)
# d= int(input("값을 입력해라\n"))+1
# for a in range(1,d):
#     b="*"*(2*a-1)
#     c=" "*(5-a)
#     print(c+b+c)
ans = int(input("시작 값을 입력하세요\n"))
user_ans= int(input("마지막 값을 입력하세요\n"))
for a in range(ans, user_ans):
    star="*"*(2*(user_ans-a)+1)
    gap=" "*(a-1)
    print(gap+star+gap)

