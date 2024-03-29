
#첫째 줄에 테스트 케이스의 개수 T가 주어진다. 
T = int(input().rstrip())

# 각 테스트 케이스에 대해 반복
for _ in range(T):
  # 현재 테스트 케이스의 달러 금액을 가져온다
  dollar = int(input())
  
  # 25로 나누어 쿼터의 수를 계산하고 출력
  # 'end' 파라미터는 출력을 같은 줄에 공백 출력
  print(int(dollar // 25), end = ' ')
  
  # 쿼터의 가치를 뺀 나머지 금액으로 금액을 업데이트
  dollar %= 25
  
  # 업데이트된 금액으로 다임의 수를 계산하고 출력
  print(int(dollar // 10), end = ' ')
  
  # 다임의 가치를 뺀 나머지 금액으로 금액을 업데이트
  dollar %= 10
  
  # 업데이트된 금액으로 니켈의 수를 계산하고 출력
  print(int(dollar // 5), end = ' ')
  
  # 니켈의 가치를 뺀 나머지 금액으로 금액을 업데이트합
  dollar %= 5
  
  # 남은 금액으로 페니의 수를 계산하고 출력
  print(int(dollar // 1), end = ' ')
  
  # 현재 테스트 케이스의 계산이 끝난 후 다음 줄로 넘어간다
  print()

