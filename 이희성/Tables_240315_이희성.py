# 단순계산문제다, 모든 테이블을 만드는데 필요한 총 나사의 개수를 계산한 후, 주어진 박스들을 나사의 개수가 많은 순서대로 정렬한 후, 필요한 박스들의 개수를 구하자

# the number of boxes with screws, the number of screws needed to make a table, the number of tables to be made
n, k, s = map(int, input().split())

total_screws = k*s  # 모든 테이블을 만드는데 필요한 총 나사의 개수

list_screws = sorted(list(map(int, input().split())), reverse=True)  # 주어진 박스들을 나사의 개수가 많은 순서대로 정렬

# 필요한 박스들의 개수를 출력
for i in range(n):
    
    # 박스들의 나사의 개수가, 필요한 총 나사의 개수보다 같거나 클 때의 박스들의 개수를 출력
    if sum(list_screws[:i+1]) >= total_screws:
        print(len(list_screws[:i+1]))
        break
