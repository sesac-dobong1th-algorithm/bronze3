#자석의 개수 N 만큼 입력받기
N = int(input())

#두 번째 줄은 관빈이가 가지고 있는 자석의 현재 연결 상태를 나타낸다
#(+)극은 1, (-)극은 2를 뜻함
magnet = input()
connected = 'Yes'

#자석이 연결
for index in range(0, len(magnet)-2, 2):
    if magnet[index] != magnet[index+2] : #자석이 연결 됐을 경우와 안됬을 경우를 정함
        connected = 'No'
        break #자석이 하나라도 분리가 된다면 for문 탈출

#연결 상태를 출력
print(connected)
