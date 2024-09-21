#9461
triangle = [0] * 101
triangle[1] = 1
triangle[2] = 1
triangle[3] = 1
triangle[4] = 2
triangle[5] = 2

for i in range(6,101):
    triangle[i] = triangle[i-1] + triangle[i-5]

p = int(input())
while p>0:
    n = int(input())
    print(triangle[n])
    p-=1
