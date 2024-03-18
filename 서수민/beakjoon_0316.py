# 사용자로부터 정수 N을 입력받음
N = int(input()) 

# 세로
# N*4만큼 반복 (세로 길이를 N의 4배로 설정)
for i in range(N*4): 
# '@' 문자를 N번 반복하여 출력 (가로 길이 N)
    print('@'*N)

# 가로
# N만큼 반복 (세로 길이 N)
for i in range(N): 
# '@' 문자를 5*N번 반복하여 출력 (가로 길이 5*N)
    print('@'*5*N) 


