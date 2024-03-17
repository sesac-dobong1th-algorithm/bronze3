# 여러번 코드를 수정해봤는데 정답을 맞추지 못했습니다. 지금까지 수정한 코드를 먼저 제출하고, 추후 정답에 맞게 수정하도록 하겠습니다.

data = open(0)
l = []
while True:
    try:   
        text = next(data)
        text = text.lower()
        a = '' 
        for i in range(len(text)):
                        
            if text[i].isalpha():            
                
                if (i == 0) and (len(l) >= 1) and (l[len(l)-1][-1] == '\n') and (l[len(l)-1][-2] in '.!?'):
                    a += text[i].upper()
                elif (text[i-2:i-1] in '.!?') and (text[i-1:i] in ' ()'):
                    a += text[i].upper()        
                else: a += text[i]
                
            else: a += text[i]
            
            if i+1 == len(text):
                l.append(a)
    except:
        break            

print(*l, sep='')
