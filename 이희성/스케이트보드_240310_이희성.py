# 처음 제출할 때 input()을 사용해서 제출했는데, 입력 데이터가 많아서그런지 채점 시간이 매우 오래걸렸다
# open(0)과 next()를 사용했고, 풀이과정도 다시 생각해보면서 코드를 작성해봤다

all_data = open(0)  # 모든 입력줄

N = int(next(all_data))  # 사람의 수

# 우승자의 최종 점수를 출력
winner_score = 0  

for _ in range(N):
    list_scores = list(map(int,next(all_data).split()))
    player_score = sum(sorted(list_scores[:2])[-1:] + sorted(list_scores[2:])[-2:])
    winner_score = max(winner_score, player_score) 

print(winner_score)

# 아래의 함수를 사용하면
# import heapq as h

# player_score = sum(sorted(list_scores[:2])[-1:] + sorted(list_scores[2:])[-2:])

# 위 코드를 아래처럼 작성할 수 있다    
# player_score = sum(h.nlargest(1,list_scores[:2]) + h.nlargest(2,list_scores[2:]))


# 아래 코드들은 위에 코드를 작성하기 전에 제출했던 코드들이다

# 첫번째 제출코드

N = int(input())
scores = []

for _ in range(N):
    score_list = list(map(int, input().split()))
    list_a = []
    list_b = []
    score = 0
        
    for i in range(2):
        list_a.append(score_list[i])  
        list_a.sort(reverse=True)
    score = list_a[0]
    
    for i in range(2,7):
        list_b.append(score_list[i])  
        list_b.sort(reverse=True)
         
    for i in range(2):
        score += list_b[i]
    
    scores.append(score)

print(max(scores))        

# 두번째 제출코드

N = int(input())
scores = []

for _ in range(N):
    score = list(map(int, input().split()))
    a = score[:2]
    a.sort(reverse=True)
    
    b = score[2:]
    b.sort(reverse=True)
    
    c = a[:1] + b[:2]
    
    scores.append(sum(c))

print(max(scores))
