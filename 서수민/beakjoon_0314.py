N = int(input())
    # 상단 부분: 별의 개수가 점점 줄어듦
for i in range(N):
    print(' ' * i + '*' * (2*(N-i)-1))

# 하단 부분: 별의 개수가 점점 늘어남
for i in range(1, N):
    print(' ' * (N-i-1) + '*' * (2*i+1))
    
    