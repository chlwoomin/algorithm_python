#24511
import sys
from collections import deque
n = int(input())
queuestack = list(map(int,input().split()))
arr = list(map(int,input().split()))
m = int(input())
c = list(map(int,input().split()))
q = deque()
answer = []
for i in range(n):
    if queuestack[i] == 0:
        q.append(arr[i])
for i in range(m):
    q.appendleft(c[i])
    answer.append(q.pop())
print(*answer)