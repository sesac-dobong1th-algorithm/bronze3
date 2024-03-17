# N*5-N번째 줄을 기준으로 @의 개수가 달라진다, 전체 N*5줄을 출력하자

N = int(input())  # 정수 N(1 ≤ N ≤ 100)

# 셀의 크기가 N인 골뱅이를 출력
for i in range(N*5):

    # N*5-N번째 줄을 기준으로 @의 개수를 다르게 출력
    if i < N*5-N : print('@'*N)
    else : print('@'*N*5)
