#%%
''' sudo code : step by step
총 3번 반복한다
-> n을 입력 받는다
-> n만큼 숫자를 입력 받는다
-> 그 숫자를 전부 더한다
-> 음수인지 양수인지 0인지 비교한다
-> 출력한다.
'''


import sys

# 반복문 3개를 입력받는다.
for _ in range(3):
    n = int(sys.stdin.readline())

# 입력받는 수의 총합 초기화
    total = 0
# 반복문으로 입력받는 수 의 총합을 0이랑 비교
    for _ in range(n):
        number = int(sys.stdin.readline())
        total += number
    # 0 초과면 + 출력    
    if total > 0:
        print("+")
    # 0 미만이면 - 출력    
    elif total < 0:
        print("-")
    # 0 이랑 같으면 0 출력
    else:
        print("0")

        