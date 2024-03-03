dict_label = {1:'A', 2:'B', 3:'C', 4:'D', 0:'E' }  # '0'의 갯수로 key값을 설정한 정답 딕셔너리

# '0'의 갯수로 dict_label 인덱싱해서 정답 출력
for _ in range(3):
    print(dict_label[input().split().count('0')])
