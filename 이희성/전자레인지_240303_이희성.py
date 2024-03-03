# 1 ≤ T ≤ 10,000 
# A B C의 단위를 초로 통일하자
# A= 300, B= 60, C=10
# A B C를 횟수로 표현하기위해 각각 10으로 나눠보자
# a = 30, b = 6, c = 1
# T가 10의 배수가 아닐때는 -1를 출력하면 된다
# 세 버튼을 조작해야하는 T는 10의 배수이기 때문에 T를 10으로 나눠 t라 하자
# 최소버튼 조작 방법을 구하는 것이기 때문에 t의 범위를 각 버튼의 최솟값에 따라 나눠서 생각해보자
# 그러면 1~5, 6~29, 30이상, 이렇게 세 범위로 나눌 수 있다
# 각 범위에서 풀어보자

dic_count = {'A': 0, 'B': 0, 'C': 0}  # 최소버튼 조작의 횟수

T = int(input())  # 요리시간
t = T // 10  # 세 버튼을 조작해야하는 요리시간은 10의 배수이기 때문에 요리시간를 10으로 나눔

if T % 10 != 0: print(-1)  # 요리시간이 10의 배수가 아닐때는 -1를 출력

# 요리시간을 10으로 나눈 시간의 범위를 나눠 최소버튼 조작의 횟수를 계산
elif t >= 30:
    x = t % 30  # B와 C버튼의 조작 횟수를 계산하기 위한 요리시간을 10으로 나눈 시간을 30으로 나눴을때의 나머지
    dic_count['A'] = t // 30
    if 6 <= x < 30:
        dic_count['B'] = x // 6
        dic_count['C'] = x % 6
    else:
        dic_count['C'] = x    
    print(dic_count['A'], dic_count['B'], dic_count['C']) 

elif 6 <= t < 30:
    dic_count['B'] = t // 6
    dic_count['C'] = t % 6
    print(dic_count['A'], dic_count['B'], dic_count['C'])

else:
    dic_count['C'] = t
    print(dic_count['A'], dic_count['B'], dic_count['C'])

# 담임강사님 피드백 후 아래와 같이 코드 수정

T = int(input())  # 요리시간
list_timer = [300, 60, 10]  # 초 단위로 통일한 타이머들의 시간
list_count = []  # 최소버튼 조작 횟수  

# 최소버튼 조작 횟수 계산, 계산이 불가할 때는 -1를 출력
for timer in list_timer:      
    count, T = divmod(T, timer)
    list_count.append(count)
print(*list_count) if T == 0 else print(-1)
