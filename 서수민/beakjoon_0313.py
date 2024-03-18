# 첫째 줄에 컵의 위치를 바꾼 횟수 M 입력
m = int(input())

# 공이 처음에 위치한 컵의 번호 초기화
ball_position = 1

# 컵의 위치를 야바위 돌린 m 만큼 for문 돌리기
for _ in range(m):
    x, y = map(int, input().split())
    # 공의 위치가 변경되는 경우를 확인하고 위치 업데이트
    if x == ball_position:
        ball_position = y
    elif y == ball_position:
        ball_position = x

# 공이 위치한 컵의 번호를 출력
print(ball_position)

