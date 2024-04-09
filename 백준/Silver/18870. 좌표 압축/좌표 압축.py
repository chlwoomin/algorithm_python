#18870
import sys
def binary_search(start, end, target):
    if start>end:
        return
    mid = (start + end) // 2

    if c_arr[mid] > target:
        binary_search(start,mid-1,target)
    elif c_arr[mid] < target:
        binary_search(mid+1,end,target)
    else:
        answer.append(mid)
    
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
c_arr = set(arr)
c_arr = sorted(list(c_arr))
answer = []
for i in arr:
    binary_search(0,len(c_arr)-1,i)
print(*answer)