number_of_settings = int(input())  # 첫줄의 주어진 숫자를 str에서 int로 형변환 
possible_settings = input().split()  # 두번째줄에 주어지는 숫자들을 리스트에 담음
height_of_the_tree = int(input())  # 마지막줄에 주어지는 숫자를 str에서 int로 형변환
dict = {}  # key에 나머지와  value에 나머지에 대응하는 숫자를 담을 빈 딕셔너리를 생성
for i in range(number_of_settings):  # 첫줄의 주어진 숫자만큼 for문 반복
    dict[int(height_of_the_tree) % int(possible_settings[i])] = possible_settings[i]
# 빈 딕셔너리에 추가, 이때 나머지가 동일할 경우 key값이 중복되면서 기존에 딕셔너리에 담긴 동일한 나머지에 해당하는 value가 새로운 value로 대체된다.
# 문제에 주어진 조건을 고려하였을 때, 문제없다.
# 이 경우에 출력되는 숫자는 동일한 나머지에 대응되는 숫자들 중 마지막에 추가되는 숫자이다
print(dict[min(dict.keys())])  
# 딕셔너리에 담겨져있는 key들 중 최솟값을 인덱싱 한후, 대응하는 value를 출력.
# 출력되는 value는 세번째 숫자를 나눴을 때 나머지가 가장 적은 두번째 줄에 주어지는 숫자이다