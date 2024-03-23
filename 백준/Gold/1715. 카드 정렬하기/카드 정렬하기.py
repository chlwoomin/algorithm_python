#1715
import heapq
import sys
'''n = int(input())
num_array = []
for i in range(n):
  heapq.heappush(num_array, int(input()))'''
n = int(sys.stdin.readline())
num_array = []
for i in range(n):
  heapq.heappush(num_array, int(sys.stdin.readline()))

total = 0
for i in range(n-1):
  sum = heapq.heappop(num_array) + heapq.heappop(num_array)
  total += sum
  heapq.heappush(num_array,sum)
print(total)