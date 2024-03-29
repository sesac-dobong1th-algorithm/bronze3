# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

# 입력 예제
# 5

# 출력 예제
# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********

n = int(input())

# n을 1까지 -1씩 빼면서 반복순회하며 리스트에 저장 별이 줄어들며 찍어야 함
a = [(" " * (n - i) + "*" * (2 * i - 1)) for i in range(n, 0, -1)] + [
    # 2부터 n까지 반복순회하며 리스트에 저장 별이 증가하게 찍어야 함
    (" " * (n - i) + "*" * (2 * i - 1))
    for i in range(2, n + 1)
]
for i in a:
    print(i)

# n을 1까지 -1씩 빼면서 반복순회하며 리스트에 저장 별이 줄어들며 찍어야 함
# a = [(" " * (n - i) + "*" * (2 * i - 1)) for i in range(n, 0, -1)]

# 2부터 n까지 반복순회하며 리스트에 저장 별이 증가하게 찍어야 함
# a += [(" " * (n - i) + "*" * (2 * i - 1)) for i in range(2, n + 1)]
# for i in a:
#   print(i)

# for i in range(n, 0, -1):
#     print(" " * (n - i) + "*" * (2 * i - 1))
# for i in range(2, n + 1):
#     print(" " * (n - i) + "*" * (2 * i - 1))
