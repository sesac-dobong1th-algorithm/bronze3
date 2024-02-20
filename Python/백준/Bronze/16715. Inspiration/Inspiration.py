N = int(input())
a = {}
for num_decimal in range(2, N+1):
    sum = 0
    q= N            # 이거 하나 못해서 한시간 날림. N값 보존을위해서 변수가 3개 필요했음. N, q, quantity...
    while q:
        quantity, r = divmod(q, num_decimal)
        sum += r
        q = quantity
        
    a[num_decimal]= sum # 문법 실수 했었음. 그냥 num_decimal 하면 되는데, {num_deciaml} 이랬음. ;;


sum_list = list(a.values())
b = max(sum_list)

key_list = list(a.keys())

num = []
for key in key_list:
    if a[key] == b:
        num.append(key)
        

    

print(int(b), min(num))