# 먼저 중복된 단어제거 후, 사전 순으로 정렬한 후, 길이 순으로 정렬하자 

words = []  # N개의 단어들

# words 리스트에 N개의 단어들 추가
for i in range(int(input())):
    words.append(input())

# 중복된 단어 제거 후, 사전 순 정렬 후, 길이 순으로 정렬
set_words = set(words)
list_words = list(set_words)
list_words.sort()
list_words.sort(key=len)
print(*list_words, sep='\n')
