# 공백으로 구분된 여러 정수를 입력받아 정수 리스트로 변환 P(People)라는 변수 설정
P = list(map(int, input().split()))

# 사용자로부터 x, y, r 세 정수를 입력받음. 여기서 x와 y는 지면과 높이로 부터의 사과의 위치를 r은 사과의 반지름을 나타낸다 
x, y, r = map(int, input().split())

# 입력받은 x가 리스트 P에 존재하는지 확인
if x in P :
    # x가 리스트 P에 존재할 경우, x의 위치(index)를 찾아 출력
    # 1부터 시작하는 것을 요구했으므로 로 가정하고 +1을 함
    print(P.index(x) + 1)
else :
    # x가 리스트 P에 존재하지 않을 경우, 0을 출력
    print(0)
