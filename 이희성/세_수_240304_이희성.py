# 네개의 연산자가 들어가는 위치는 첫번째 숫자와 두번째 숫자 사이, 두번째 숫자와 세번째 숫자 사이로 두 자리가 있다
# 한 자리에 연산자가 들어가면 나머지 자리에는 등호가 들어간다
# 총 경우의 수는 2*4=8가지이다
# if-elif-else문으로 모든 경우의 수를 작성해서 풀 수 있다
# operator = ['-', '+', '*', '/'], 이런식으로 연사자들을 인덱싱해보려고 했는데, 애초에 3'+'3 이렇게 되어서 syntaxError가 발생한다
# 코드를 간략해보려고 시도해봤는데, 입력을 a, b, c 이런식으로 짧은 이름을 가진 변수들에 할당하는 방법말고는 딱히 방법이 없는 것 같다

equation = list(map(int, input().split()))  # 첫줄에 주어지는 세 정수

# 조건에 만족시키는 등식을 출력
if equation[0]+equation[1] == equation[2]:
    print(f'{equation[0]}+{equation[1]}={equation[2]}')
elif equation[0]-equation[1] == equation[2]:
    print(f'{equation[0]}-{equation[1]}={equation[2]}')
elif equation[0]*equation[1] == equation[2]:
    print(f'{equation[0]}*{equation[1]}={equation[2]}')
elif equation[0]/equation[1] == equation[2]:
    print(f'{equation[0]}/{equation[1]}={equation[2]}')
elif equation[0] == equation[1] + equation[2]:
    print(f'{equation[0]}={equation[1]}+{equation[2]}')
elif equation[0] == equation[1] - equation[2]:
    print(f'{equation[0]}={equation[1]}-{equation[2]}')
elif equation[0] == equation[1] * equation[2]:
    print(f'{equation[0]}={equation[1]}*{equation[2]}')
else : print(f'{equation[0]}={equation[1]}/{equation[2]}')
