num=int(input())  
# 첫째줄에 주어지는 숫자를 str에서 int로 형변환
for n in range(num):  
# num만큼 for 반복문을 실행
    print(" "*(num-n)+"*"*(2*n-1))  
# 공백은 두번째줄부터 한칸으로 시작해 다음줄부터 별 출력시 한칸씩 늘어난다. 첫줄에 2×n의 별이 출력되고, 두번째줄부터는 두개씩 줄어든다.
# for문에서 n은 0부터 시작한다.
