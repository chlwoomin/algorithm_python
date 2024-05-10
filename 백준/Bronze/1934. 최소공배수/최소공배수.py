#1934
import sys
import math
def com (a,b):
    arr = []
    i=2
    while i <= a and i <= b:
        if a % i == 0 and b % i == 0:
            a = a/i
            b = b/i
            arr.append(i)
        else:
            i+=1
    arr.append(a)
    arr.append(b)
    return int(math.prod(arr))
n = int(input())
for i in range(n):
    a, b = map(int,input().split())
    print(com(a,b))
