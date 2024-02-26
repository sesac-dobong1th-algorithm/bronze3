hour, minute = map(int, input().split())  # 현재 시간
cookTime = int(input())  # 요리시간

resultH = hour + (
    (minute + cookTime) // 60
)  # 현재 시 + ((현재 분+요리시간)//60) => 몫만 현재 시에 더하자
resultM = (minute + cookTime) % 60  # (현재 분+요리시간)%60 => 나머지 값은 분 결과

if resultH >= 24:  # 24시 이상일 경우
    resultH = resultH % 24  # 나머지를 최종 시간으로 출력

if resultM >= 60:  # 60분 이상일 경우
    resultM = resultM % 60  # 나머지를 최종 분으로 출력

print(resultH, resultM)
