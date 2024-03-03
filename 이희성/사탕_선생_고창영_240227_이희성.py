test_number = int(input())  # 테스트 케이스의 개수  

for _ in range(test_number):  
    # 테스트 자료
    input()  # 한줄 띄우기  
    student_number = int(input())  # 학생수
    total_candy = [int(input()) for _ in range(student_number)]  # 총캔디 개수    
    
    # 나눴을 때 나머지가 0이면 YES, 0이 아니면 NO출력
    if sum(total_candy) % student_number == 0:
        print('YES')
    else:
        print('NO')
