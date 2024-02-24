t=int(input())
for _ in range(t):
    num, unit = input().split()
    num= float(num)
    
    if unit== 'kg':
        new_num= round(num*2.2046,4)
        print(f'{new_num} lb')
    elif unit == 'l':
        new_num= round(num*0.2642,4)
        print(f'{new_num} g')
    elif unit =='lb':
        new_num =round(num*0.4536, 4)
        print(f'{new_num} kg')
    elif unit == 'g':
        new_num = round(num*3.7854,4)
        print(f'{new_num} l')