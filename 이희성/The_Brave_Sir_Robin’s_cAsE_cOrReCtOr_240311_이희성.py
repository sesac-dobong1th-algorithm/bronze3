# 정규표현식을 사용해서 풀었다
# 정규표현식이 유용하다는 것을 새삼 깨달았다

import re

def capitalize_after_punctuation(text):
    
    # 종결 부호 뒤에 오는 열고 닫는 괄호와 공백 문자와 줄바꿈 문자가 순서에 상관없이 여러 번 나올 수 있도록 처리
    # Capturing group을 사용하여 문장 종결 부호와 이후 문자들( ()\s\n )을 포함시키고, 소문자 알파벳을 대문자로 변환
    pattern = r'([?!.][()\s\n]*)([a-z])'
    return re.sub(pattern, lambda x: x.group(1) + x.group(2).upper(), text)

texts = ''

# 문제의 input file의 text를 한줄씩 소문자로 변환하고 texts에 추가
while True:
    try:
        line = input()
        texts += line.lower() + '\n'
    except :
        break

# 변환된 텍스트 출력
print(capitalize_after_punctuation(texts))

# 아래는 정답을 맞추지 못했던 코드이다

# data = open(0)
# l = []
# while True:
#     try:   
#         text = next(data)
#         text = text.lower()
#         a = '' 
#         for i in range(len(text)):
                        
#             if text[i].isalpha():            
                
#                 if (i == 0) and (len(l) >= 1) and (l[len(l)-1][-1] == '\n') and (l[len(l)-1][-2] in '.!?'):
#                     a += text[i].upper()
#                 elif (text[i-2:i-1] in '.!?') and (text[i-1:i] in ' ()'):
#                     a += text[i].upper()        
#                 else: a += text[i]
                
#             else: a += text[i]
            
#             if i+1 == len(text):
#                 l.append(a)
#     except:
#         break            

# print(*l, sep='')
