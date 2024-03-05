# N개의 정수가 주어지면, 이 정수들의 합 S의 부호를 구하는 프로그램을 작성하시오.

# 입력
# 총 3개의 테스트 셋이 주어진다. 각 테스트 셋의 첫째 줄에는 N(1 ≤ N ≤ 100,000)이 주어지고,
# 둘째 줄부터 N개의 줄에 걸쳐 각 정수가 주어진다. 주어지는 정수의 절댓값은 9223372036854775807보다 작거나 같다.

# 출력
# 총 3개의 줄에 걸쳐 각 테스트 셋에 대해 N개의 정수들의 합 S의 부호를 출력한다.
# S=0이면 "0"을, S>0이면 "+"를, S<0이면 "-"를 출력하면 된다.

import sys

input = sys.stdin.readline  # 문자열 하나씩 입력받기(시간 초과 방지)

result = []  # 최종 결과 저장 빈 리스트
for _ in range(3):  # 3번 반복
    n = int(input())  # 반복마다 입력할 정수 값 초기화
    s = [
        int(input()) for _ in range(n)
    ]  # n번 만큼 반복하여 정수 입력하여 s에 리스트로 저장
    if sum(s) == 0:
        result.append(0)  # s의 합이 0이면 result에 0저장
    elif sum(s) > 0:
        result.append("+")  # s가 0보다 크면 result에 +저장
    else:
        result.append("-")  # s가 0보다 작으면 result에 -저장

# 최종 출력
for i in result:
    print(i)
