all_data = open(0)  # 모든 입력을 받음

for _ in range(int(next(all_data))):  # 문제수만큼 for문 반복
    question = next(all_data)  # 문제 
    
    # 문제에 + 기호가 있으면 두 숫자를 계산한 결과를 출력하고, 그렇지않은 경우(P=NP)에는 skipped를 출력
    if '+' in question:
        print(sum(map(int,question.split('+'))))
    else:
        print('skipped')
