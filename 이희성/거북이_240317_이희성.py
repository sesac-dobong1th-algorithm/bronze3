# 직사각형을 만들 수 있는, 최대한 큰 숫자 두개를 찾자
# 거북이의 움직임을 순서대로 가로1, 세로1, 가로2, 세로2라고 할 때, 가로1 >= 가로2, 세로1 <= 세로2이어야 한다
# 가장 큰 직사각형을 만들기 위해 우선 가로1을 가장 큰 숫자로 한 후, 나머지 숫자들을 생각해보면,
# 세로1에는 세번째로 큰 숫자와 가장 작은 숫자가 가능한데,
# 세로1에 세번째로 큰 숫자가 올 경우 가로2에는 가장 작은 숫자가 오기 때문에, 가장 큰 직사각형을 만들기 위해 가장 작은 숫자가 세로1이 된다
# 이때 가로2와 세로2에는 나머지 두개의 숫자가 가능한데, 가장 큰 직사각형을 만들기 위해 두번째 큰 숫자가 가로2가 된다
# 가로1 >= 가로2, 세로1 <= 세로2 이 조건에 의해, 넓이는 가로2*세로1이 된다

list_number = sorted(list(map(int, input().split())))  # 거북이가 생각한 네 양의 정수를 오름차순으로 정렬

# 거북이가 만들 수 있는 가장 큰 직사각형의 면적을 출력
print(list_number[0]*list_number[2])

# 아래는 처음 문제를 풀 때 모든 경우의 수를 고려해서 작성한 코드다

# A, B, C, D = map(int, input().split())
# l = []

# if (A >= B) and (C <= D): l.append(B*C)
# if (A >= B) and (D <= C): l.append(B*D)
# if (A >= C) and (B <= D): l.append(C*B)
# if (A >= C) and (D <= B): l.append(C*D)
# if (A >= D) and (B <= C): l.append(D*B)
# if (A >= D) and (C <= B): l.append(D*C)

# if (B >= A) and (C <= D): l.append(A*C)
# if (B >= A) and (D <= C): l.append(A*D)
# if (B >= C) and (A <= D): l.append(C*A)
# if (B >= C) and (D <= A): l.append(C*D)
# if (B >= D) and (A <= C): l.append(D*A)
# if (B >= D) and (C <= A): l.append(D*C)

# if (C >= A) and (B <= D): l.append(A*B)
# if (C >= A) and (D <= B): l.append(A*D)
# if (C >= B) and (A <= D): l.append(B*A)
# if (C >= B) and (D <= A): l.append(B*D)
# if (C >= D) and (A <= B): l.append(D*A)
# if (C >= D) and (B <= A): l.append(D*B)

# if (D >= A) and (B <= C): l.append(A*B)
# if (D >= A) and (C <= B): l.append(A*C)
# if (D >= B) and (A <= C): l.append(B*A)
# if (D >= B) and (C <= A): l.append(B*C)
# if (D >= C) and (A <= B): l.append(C*A)
# if (D >= C) and (B <= A): l.append(C*B)

# print(max(l))
