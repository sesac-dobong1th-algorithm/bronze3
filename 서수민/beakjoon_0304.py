# 사용자로부터 세 정수 a, b, c 입력 받기
a, b, c = map(int, input().split())

# a와 b의 합이 c와 같은지 확인
if a+b == c:
    print(f"{a}+{b}={c}")
# a에서 b를 뺀 값이 c와 같은지 확인
elif a-b == c:
    print(f"{a}-{b}={c}")
# a와 b의 곱이 c와 같은지 확인
elif a*b == c:
    print(f"{a}*{b}={c}")
# a를 b로 나눈 몫이 c와 같은지 확인
elif a//b == c:
    print(f"{a}/{b}={c}")
# a가 b와 c의 합과 같은지 확인
elif a == b+c:
    print(f"{a}={b}+{c}")
# a가 b에서 c를 뺀 값과 같은지 확인
elif a == b-c:
    print(f"{a}={b}-{c}")
# a가 b와 c의 곱과 같은지 확인
elif a == b*c:
    print(f"{a}={b}*{c}")
# a가 b를 c로 나눈 몫과 같은지 확인
elif a == b//c:
    print(f"{a}={b}/{c}")

    # 다시 시도

