# 일단 기본료를 각각 10원, 15원으로 하고
# (a // 30) * 10
# (b // 60) * 15 이런식으로 추가
# 근데 그냥 (a // 30 + 1) * 10 이런식으로 하면 기본료 따로 고려안해도 된다

# all_data = open(0)  # 입력이 두줄뿐이라 open()은 사용안해도 될듯
# next(all_data)
# call_time = list(map(int, next(all_data).split()))  # 리스트컴프리헨션으로 해보자
# fee_y = sum([(i // 30 + 1) * 10 for i in call_time])
# fee_m = sum([(i // 60 + 1) * 15 for i in call_time])
# if fee_y < fee_m:
#     print('Y', fee_y)
# elif fee_y == fee_m:
#     print('YM', fee_y)  # 문제랑 예제 입력 1만 보고, YM 사이에 공백이 없을거라고 생각 
# else:
#     print('M', fee_m)

# input()
# call_time = [x for x in map(int, input().split())]
# fee_y = sum([(i // 30 + 1) * 10 for i in call_time])  # +=로 해보자 
# fee_m = sum([(i // 60 + 1) * 15 for i in call_time])
# if fee_y < fee_m:
#     print('Y', fee_y)
# elif fee_y == fee_m:
#     print('Y','M', fee_y)
# else:
#     print('M', fee_m)

input()  # 줄띄움
fee_y=fee_m=0  # 영식과 민식의 요금제

# 동호의 통화 자료로부터 영식과 민식의 요금제 계산
for call in map(int, input().split()):  
    fee_y += (call // 30 + 1) * 10
    fee_m += (call // 60 + 1) * 15

# 영식 요금제와 민식 요금제 비교
if fee_y < fee_m:
    print('Y', fee_y)
elif fee_y == fee_m:
    print('Y','M', fee_y)
else:
    print('M', fee_m)
