#1912
n = int(input())
number = list(map(int,input().split()))
s = [number[0]]
for i in range(1,n):
    s.append(max(number[i],s[i-1]+number[i]))
print(max(s))