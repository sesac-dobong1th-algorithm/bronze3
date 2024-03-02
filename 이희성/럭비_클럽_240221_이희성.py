while True:  # 무한루프를 실행
    profile = input().split()  # 주어진 입력을 받아 공백을 기준으로 나눈 자료들이 들어간 리스트를 profile 변수에 할당
    profile_name = profile[0]  # 인덱싱으로 이름을 profile_name에 할당
    profile_age = int(profile[1])  # 인덱싱 후 나이를 str에서 int로 형변환 후 profile_age에 할당
    profile_weight = int(profile[2])  # 인덱싱 후 몸무게를 str에서 int로 형변환 후 profile_weight에 할당
    if profile_age == 0:  # 나이가 0이면 반복문을 종료, 이 조건문의 위치를 마지막으로 하면 안됨
        break
    elif profile_age > 17 or profile_weight >= 80:  # 문제에 주어진 성인부 조건을 만족하면 이름 Senior을 출력, 성인부 조건은 나이와 몸무게 두 조건중 하나만 충족하면 되기 때문에 or 연산자를 사용
        print(f'{profile_name} Senior')
    else:  # 문제에 주어진 성인부 조건을 만족하지 못하면 이름 Senior을 출력
        print(f'{profile_name} Junior')
        