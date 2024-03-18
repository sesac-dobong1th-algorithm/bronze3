# 각줄의 별의 개수를 계산한 후, .center() 함수를 사용해 중앙으로 정렬하고, .rstrip() 함수를 사용해 오른쪽 공백을 제거해준다

N = int(input())  # (1 ≤ N ≤ 100)

# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력
for i in range(N*2-1):
    if i < N:
        star = '*'*((N-i-1)*2+1)
        print(star.center(N*2-1).rstrip())
    else:
        star = '*'*((i+1-N)*2+1)
        print(star.center(N*2-1).rstrip())
