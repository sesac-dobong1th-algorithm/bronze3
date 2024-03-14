# 수정된 코드를 실행하여 올바른 출력 결과 확인
output_corrected = []
for i in range(9,0,-2):
    output_corrected.append('{:^10}'.format('*'*i))

for i in range(3,11,2):
    output_corrected.append('{:^10}'.format('*'*i))

output_corrected
