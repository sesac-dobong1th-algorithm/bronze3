# 두번째줄부터 얼룩말 정보들을 1집단과 0 집단으로 나눈 후,
# 1집단의 최대갯수를 구하고 최대갯수의 1집단을 가진 얼룩말 정보들의 갯수를 구한다

# 첫째줄에 주어지는 두 숫자들 중 필요한 개체수 숫자만 n으로 할당
n = int(input().split()[0])
# 얼룩말의 줄의 갯수를 담을 빈리스트를 생성
stripe = []
# 1집단들과 모든0이 ''으로 담긴 black에서 ''을 제외한 1집단들만 다시 black_cleand에 담은 후,
# 얼룩말 줄의 갯수인 black-cleand의 길이를 stripe에 담는다
for _ in range(n):
    black = input().split('0')
    black_cleaned = [x for x in black if x != '']
    stripe.append(len(black_cleaned))
# 문제에서 요구하는 검은 줄의 개수와 얼룩말의 개체수를 공백으로 구분하여 출력
print(max(stripe),stripe.count(max(stripe)))