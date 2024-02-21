n = int(input())
import sys
num_list = list(map(int, sys.stdin.readline().split()))


for m in range(2,10**9+1):
        t_list = list(map(lambda x: x % m, num_list))

        k = max(set(t_list), key = t_list.count)
        
       
        count = t_list.count(k)  # 여기서 t_list가 아니라, num_list로 잘못 씀... 실수...
       
        if count >= n/2 and m > k:
                print(m, k)
                break