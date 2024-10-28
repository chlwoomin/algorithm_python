#11054
n = int(input())
arr = list(map(int, input().split()))
increase = [1] * n
decrease = [1] * n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            increase[i] = max(increase[i], increase[j] + 1)
        if arr[n-1-i] > arr[n-1-j]:
            decrease[n-1-i] = max(decrease[n-1-i], decrease[n-1-j] + 1)
res = [increase[i] + decrease[i] for i in range(n)]
print(max(res) - 1)