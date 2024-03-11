def process_text(input_text):
    # 결과 문자열을 저장할 변수 초기화
    result = ''
    
    # 첫 문자를 소문자로 변환하여 추가
    if input_text:
        result += input_text[0].lower()
    
    i = 1  # 현재 문자를 가리키는 인덱스
    # 문자열을 순회하면서 조건에 따라 문자 변환
    while i < len(input_text):
        # 구두점 뒤 첫 비공백 문자를 대문자로 변환
        if input_text[i-1] in '.?!' and not input_text[i].isspace():
            result += input_text[i].upper()
        else:
            result += input_text[i].lower()
        
        i += 1
        
        # 구두점 다음 공백을 건너뛰고 첫 비공백 문자를 대문자로 변환
        if result[-1] in '.?!':
            while i < len(input_text) and input_text[i].isspace():
                result += input_text[i]
                i += 1
            if i < len(input_text):
                result += input_text[i].upper()
                i += 1

    return result

# 사용자로부터 입력을 받음
user_input = input()

# 입력된 텍스트를 처리
processed_text = process_text(user_input)

# 처리된 텍스트를 출력
print(processed_text)


