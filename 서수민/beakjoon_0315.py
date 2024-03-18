n, k, s = map(int, input().split())
total = k * s  # 총 필요 나사 수
boxes = list(map(int, input().split()))  # 상자별 나사 수

boxes.sort(reverse=True)

cnt = 0  # 필요 상자 수
sum = 0  # 현재까지 나사 수

for b in boxes:
    sum += b
    cnt += 1
    if sum >= total:
        print(cnt)
        break
    
    
    