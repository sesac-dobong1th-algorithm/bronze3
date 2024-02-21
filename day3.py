while True:
  name, age, w = input().split()
  name, age, w = str(name), int(age), int(w)
  if (name == '#') & (age==0) & (w==0):
    break
  if age > 17 or w >=80:
    print(f'{name} Senior')
  else:
    print(f'{name} Junior')

'''
질문 1
input받은 값들의 형변환을 if문에서 해야하는지 if문 전에 해야하는지

질문 2
&
AND 의 차이


'''