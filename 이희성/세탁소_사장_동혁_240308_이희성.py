# 전자레인지 문제와 동일한 문제다

n = int(input())  # 테스트 케이스 개수
list_coins = [25, 10, 5, 1]  # 거스름돈으로 줄 동전들의 단위 

# 거스름돈으로 줄 4개의 동전들의 개수 계산
for _ in range(n):
    money = int(input())
    list_count = []
    for coin in list_coins:
        count, money = divmod(money, coin)
        list_count.append(count)
    print(*list_count)
