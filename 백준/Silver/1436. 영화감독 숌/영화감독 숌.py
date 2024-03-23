#1436
b_cnt = 0
def in6(x):
  global cnt
  if '6' in x:
    for i in range(x.find('6'),len(x)):
      if x[i] == '6':
        cnt+=1
      elif '6' in x[i:]:
        i = x.find('6')
        cnt=0
      elif '6' not in x[i:]:
        break
      if cnt>=3:
        break

n = int(input())
arr = []
x=666
while True:
  cnt=0
  in6(str(x))
  if cnt >= 3:
    arr.append(x)
    b_cnt+=1
    cnt = 0
  if b_cnt == n:
    break
  x+=1

print(arr[n-1])