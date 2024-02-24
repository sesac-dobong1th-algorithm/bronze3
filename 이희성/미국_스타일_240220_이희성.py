table1 = {'kg': 2.2046, 'lb': 0.4536, 'l': 0.2642, 'g': 3.7854}  # key는 단위, value는 주어진 숫자를 value에 대응하는 단위로 변환할 때 곱할 숫자
table2 = {'kg': 'lb', 'lb': 'kg', 'l': 'g', 'g': 'l'}  # key는 단위, value는 변환된 숫자에 해당하는 단위
for _ in range(int(input())):  # 첫째줄의 숫자를 str에서 int로 형변환 한 후 해당 숫자만큼 for 반복문을 실행
    n, s = input().split()  # 둘째줄부터 주어지는 숫자와 단위를 공백을 기준으로 리스트안에 각각 담고, n과 s에 할당
    n = float(n)  # n을 str에서 float으로 형변환   
    if s in table1:  # s가 table1에 있으면 if문 실행
        print(f'{n*table1[s]:0.4f} {table2[s]}')  # 반올림해서 소숫점 넷째자리까지 표현한 변환된 숫자와 변환된 숫자의 단위를 출력