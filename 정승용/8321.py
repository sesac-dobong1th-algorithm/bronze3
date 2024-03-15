# Byteman works as a carpenter. He has just received an order for s pine-wood tables.
# Although he has plenty of pine-wood boards in his workshop, he has just run out of screws.
# Therefore he needs to walk to the warehouse and bring back some boxes with screws.
# What is the minimum number of boxes that he needs to bring in order to have enough
# screws to make the tables?

# 입력
# The first line of the standard input contains three integers n, k and s (1 ≤ n, k, s ≤ 1 000)
# separated with single spaces. They denote the number of boxes with screws in Byteman's warehouse,
# the number of screws needed to make a table and the number of tables to be made by Byteman,
# respectively. The second line contains n (not necessarily different) integers ai (1 ≤ ai ≤ 1 000)
# separated with single spaces, such that ai is the number of screws in the ith box in the warehouse.

# 출력
# The first and only line of the standard output should contain a single integer -
# the minimal number of boxes with screws that Byteman needs to bring from his warehouse
# in order to make s tables. You may assume that Byteman has enough screws in the warehouse
# to make all tables.

# n 상자 수
# k 테이블 당 필요한 나사 수
# s 만들 테이블 수

n, k, s = map(int, input().split())
ks = k * s  # 필요한 전체 나사 수
a = list(map(int, input().split()))  # 상자에 들어있는 나사 수
a.sort(reverse=True)

for i in range(n):  # n번 반복
    ks -= a[i]  # 들어있는 나사 수만큼 뺀다
    if ks <= 0:  # 필요 나사수가 0이거나 0보다 작을 때
        print(len(a[: i + 1]))  # 결과 출력
        break
