#각 변에 점이 2**n개 만큼 증가
# N 전 만큼 입력을 받음
 #N = int(input())

n = 2
a = 1
for i in range(int(input())):
    n += a
    a *= 2
print(n**2)



