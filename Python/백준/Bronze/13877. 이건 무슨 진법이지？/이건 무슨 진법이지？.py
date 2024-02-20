import sys
T = int(input())  
each_line_info = [sys.stdin.readline().strip() for i in range(T)] # a = ["1 23", "2 56"]

def to_8(x):
    if '8' in x or '9'in x:
        return 0
            
    else:
        result = [int(int(x[number])*8**(len(x)-1-number)) for number in range(len(x))]
        return sum(result)
       
def to_16(x):
    result = [int(int(x[number])*16**(len(x)-1-number)) for number in range(len(x))]
    return sum(result)

for i in each_line_info:
    
    K, numbers = i.split()
    
    print(int(K), int(to_8(numbers)), int(numbers), int(to_16(numbers)))