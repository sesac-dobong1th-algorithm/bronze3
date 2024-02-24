# 역에서 내린 사람 수를 a 탄 사람 수를 b라고 하면, 역에서는 (b - a)만큼 인원변동이 생긴다
# 기차가 도착할 때 인원변동이 생긴다고 가정하고 계산한다
# 역에 기차가 도착할 때의 기차안의 사람 수는, 역에 도착하기 전 기차안의 사람 수에 (b - a)을 계산해주면 된다  
list_count_people = []  # 각 역에서 기차안의 사람 수를 담을 빈 리스트를 생성
a, b = map(int, input().split())  # 첫줄에 주어지는 두개의 숫자를 str에서 int로 형변환 후 a, b에 할당
list_count_people.append(b - a)  # 첫번째 역의 기차안의 사람 수를 계산해서 리스트에 추가
for i in range(9):  # for 반복문을 9번 실행
    a, b = map(int, input().split())  # 각 줄마다 주어지는 두개의 숫자를 str에서 int로 형변환 후 a, b에 할당
    list_count_people.append(list_count_people[i] + (b - a))  # 각 역에서 기차안의 사람 수를 계산해서 리스트에 추가
print(max(list_count_people))  # 기차에 사람이 가장 많을 때의 사람 수를 출력