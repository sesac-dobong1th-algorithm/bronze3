# 문제는 길지만, 필요한 정보는 사과의 중심의 x좌표 하나이다

people_location = list(map(int, input().split()))  # 사람들의 위치
x, y, r = map(int, input().split())  # 사과의 정보

# 사과의 중심의 x좌표와 일치하는 사람의 번호를 출력, 없으면 0을 출력
if x in people_location:
    print(people_location.index(x)+1)
else: print(0)
