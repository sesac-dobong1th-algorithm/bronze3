# 사용자로부터 경기 참가자 수 N을 입력받음
N = int(input())
result = 0  # 최대 점수를 저장할 변수 초기화

# N명의 참가자에 대해 반복
for _ in range(N):
    # 참가자의 점수를 입력받아 정수 리스트로 변환
    Game = list(map(int,input().split()))
    # 리스트에서 런(Run) 점수와 기술(Skill) 점수를 분리
    R = Game[:2]
    Skill = Game[2:]

    # 런 점수를 내림차순으로 정렬
    R.sort(reverse=True)
    # 트릭 점수를 내림차순으로 정렬
    Skill.sort(reverse=True)

    # 현재 참가자의 최대 점수(가장 높은 런 점수 + 상위 2개 트릭 점수의 합)를 계산
    # 그리고 이전까지의 최대 점수와 비교하여 더 큰 값을 result에 저장
    result = max(result, R[0] + sum(Skill[:2]))

# 모든 참가자를 검토한 후 최대 점수 출력
print(result)

