# 문제에 주어진 E의 최댓값이 62이므로 2^62가 문제에서 나올 수 있는 최대숫자라고 판단했다
# 아래의 NOTE와 관련해 검색해 봤는데, 
# 파이썬에서는 고려하지 않아도 될 것 같다
# NOTE: The value of 2^44 does not fit in a normal 32-bit integer.

# Python의 int 자료형은 어떻게 범위가 무제한일까? 🤔

# 💡 파이썬의 정수 자료형은 하나의 객체이다.
# 💡 파이썬은 이 객체 내부에서 정수를 배열로 변환해 저장한다.
# 💡 배열 안의 값들은 2^30의 값을 벗어나지 않으므로, 정수 오버플로가 발생하지 않는다.
# 💡 따라서, 배열을 계속 확장하면 이론상 무한한 크기의 정수를 표현할 수 있다.

# 숫자를 인덱싱 할 수는 없으므로 문자로 형변환 후 인덱싱 하면 된다

# a = [str(pow(2,i+1))[0] for i in range(62)]
# 2 4 8 1 3 6 1 2 5 1 2 4 8 1 3 6 1 2 5 1 ...
# 2의 거듭제곱들의 첫자리 숫자들을 살펴보았는데, 규칙이 있어보이진 않는다
# len(set(a)) = 9 > 2의 거듭제곱들의 첫자리 숫자들은 1~9까지 있다

# 문제를 아래와 같이 요약해봤다
# A (0 <= A <= 45) and B (1 <= B <= 9) and E (1 <= E <= 62)
# if A < E & B == the first deigit of 2^E return the smallest E else return 0

# 문제의 조건을 간략하게 코드로 구현해보았다
# if A < E & str(pow(2,E))[0] == B: return E
# else: return 0

# 아래부터 코드를 작성해서 풀어보는 과정이다

# A, B = input().split()
# list_E=[]  # 리스트 컴프리헨션으로 해보자
# for E in range(62):
#     if (A < str(E+1)) & (str(pow(2,E+1))[0] == B):
#        list_E.append(E+1)
# if list_E:
#     print(min(list_E))
# else:
#     print(0)

# A, B = input().split()
# list_E = [E+1 for E in range(62) if (A < str(E+1)) & (str(pow(2,E+1))[0] == B)]
# if list_E: print(min(list_E))
# else: print(0)

# 위에 코드를 제출했는데, 틀렸다고 나와서 오랜시간 고민을 했다
# 담임강사님의 피드백을 통해 해결할 수 있었다
# if (A < str(E+1))
# 위 조건문은 숫자들을 int가 아닌 str상태에서 비교를 하는데, 한자리 숫자일 때는 문제가 없지만,
# 두자리 숫자 이상일 때는 다음과 같은 비교에서 True가 나오는 문제가 발생한다
# '23' < '3'
# 파이썬에서는 두개의 문자열을 비교할 때 각 문자열의 첫째자리부터 사전식으로 비교를 하기 때문이다
# 처음에 풀 때 '3' < '7' 와 같이 한자리 숫자들만 비교해보고, 문제가 없을줄 알았다

# 아래는 수정한 코드이다

A, B = input().split()  # 문제에 주어진 첫줄의 두 숫자를 A와B에 할당

# A보다 크고, 2^E의 첫자리가 B와 같은 E를 list_E에 담음. 그러한 E가 없을 경우 list_E는 빈리스트가 된다
list_E = [E+1 for E in range(int(A), 62) if str(pow(2,E+1))[0] == B]

# list_E에 담긴 E들중 가장 작은 E를 출력, 그러한 E가 없을 경우 0을 출력
if list_E: print(min(list_E))
else: print(0)

# 아래 코드는 구글링해서 찾아본 다른 사람이 푼 코드이다, 문제 풀면서 저런 방식도 생각해봤는데,
# if문에서 조건에 맞는 E가 처음 나올 때 for문을 끝내는 break이 떠오르지 않아서 위와 같이 풀게 되었다

# A, B = map(int, input().split())
# res = 0
# for i in range(A+1, 63):
#     if int(str(2**i)[0]) == B:
#         res = i
#         break
# print(res)

# 함수랑 클래스로 작성해봤다

def calculate(A, B):
    list_E = [E+1 for E in range(int(A), 62) if str(pow(2,E+1))[0] == B]
    if list_E: return (min(list_E))
    else: return 0

A, B = input().split()
E = calculate(A, B)
print(E)

class Solution():
    def calculate(self, A, B):
        list_E = [E+1 for E in range(int(A), 62) if str(pow(2,E+1))[0] == B]
        if list_E: return (min(list_E))
        else: return 0

A, B = input().split()
E = Solution().calculate(A, B)
print(E)
