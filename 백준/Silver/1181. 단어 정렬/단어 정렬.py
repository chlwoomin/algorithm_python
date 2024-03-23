#1181
n = int(input())
arr = [input() for _ in range(n)]
answer = []
for i in range(len(max(arr,key=len))):
  answer.append([])
  for j in range(len(arr)):
    if len(arr[j]) == i+1:
      answer[i].append(arr[j])
for i in answer:
  i = list(set(i))
  i.sort()
  for x in i:
    print(x)