# 사용자로부터 입력받기
n = list(map(int, input().split()))

# 리스트를 오름차순으로 정렬
n = sorted(n)

# 정렬된 리스트의 첫 번째와 세 번째의 곱을 출력
print(n[0] * n[2])


