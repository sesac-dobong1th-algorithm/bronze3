n = int(input())  # 입력받을 n값
h = list(map(int, input().split()))  # n개의 나눌값
t = int(input())  # tree 높이

r = 0  # t % i의 나머지값
n = []  # 나머지 값들을 저장할 리스트
s = 0  # 최종 결과물 비교용

# 리스트 저장
for i in h:
    r = t % i
    n.append(r)
    # if min(n) == r:
    #     s = i

# 리스트 내의 데이터와 비교
for i in h:
    r = t % i
    if min(n) == r:
        s = i

# 결과
print(s)
