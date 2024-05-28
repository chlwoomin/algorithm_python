#2164
from collections import deque
n = int(input())
answer = deque()
for i in range(n):
    answer.append(i+1)

while len(answer) > 1:
    answer.popleft()
    answer.append(answer.popleft())
print(*answer)