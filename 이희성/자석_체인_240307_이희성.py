number = int(input())  # 자석의 개수
magnetics = input()  # 자석의 현재 연결 상태

# 자석이 모두 연결되어있으면 "Yes", 모두 연결되어 있지 않은 상태라면 "No"를 한 줄에 출력
for n in range(number-1) :
    magnetic1 = magnetics[2*n:2*(n+1)]
    magnetic2 = magnetics[2*(n+1):2*(n+2)]
    if magnetic1 != magnetic2 :
        print('No')
        break
    if n == number-2:
        print('Yes')
