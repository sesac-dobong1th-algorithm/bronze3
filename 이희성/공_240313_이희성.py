# 두번째줄부터 공이 들어있는 컵을 찾아 공이 들어있는 컵의 번호를 바꿔주면 된다

N = int(input())  # 컵의 위치를 바꾼 횟수
B = 1  # 공이 들어있는 컵의 번호

# 공이 들어있는 컵의 번호를 출력
for _ in range(N):
    a, b = map(int, input().split())
    if a == B:
        B = b
    elif b == B:
        B = a
print(B)
