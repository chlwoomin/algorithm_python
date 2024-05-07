#1764
import sys
n ,m = map(int,sys.stdin.readline().split())
a_set = set()
b_set = set()
for i in range(n):
    a_set.add(sys.stdin.readline().strip())
for i in range(m):
    b_set.add(sys.stdin.readline().strip())
answer = sorted(a_set & b_set)
print(len(answer))
for i in answer:
    print(i)