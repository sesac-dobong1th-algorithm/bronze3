# 첫째줄에 컵의 위치를 바꾼 m 입력
m = int(input())

# 야바위 컵의 개수 생성 
cup = [1, 2, 3]

# 컵의 위치를 야바위 돌린 m 만큼 for문 돌리기 
for _ in range(m) :
    x, y = map(int, input(). split())
# # 선택된 두 컵의 위치를 교환
    if cup.index(x) < 3 and cup.index(y) < 3:  # 컵의 인덱스가 유효한지 확인
        cup[cup.index(x)], cup[cup.index(y)] = cup[cup.index(y)], cup[cup.index(x)]
    
# print(cup)
## 공이 위치한 컵의 번호를 출력(인덱스는 0부터 시작하므로, 출력 시 +1)
print(cup.index(1)+1)

