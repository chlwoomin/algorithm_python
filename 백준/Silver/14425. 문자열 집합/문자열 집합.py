#14425
n,m = map(int,input().split())
a_set = set()
answer = 0
for i in range(n):
    a_set.add(input())
for i in range(m):
    if input() in a_set:
        answer+=1
print(answer)