#10815
import sys
def binary_search (start,end,target):
    if start>end:
        answer.append(0)
        return
    mid = (start + end) // 2
    
    if hand_card[mid] > target:
        binary_search(start,mid-1,target)
    elif hand_card[mid] < target:
        binary_search(mid+1,end,target)
    else:
        answer.append(1)
        return 
answer=[]
n = int(sys.stdin.readline())
hand_card = list(map(int,sys.stdin.readline().split()))
hand_card.sort()

m = int(sys.stdin.readline())
c_card = list(map(int,sys.stdin.readline().split()))

for i in c_card:
    binary_search(0,len(hand_card)-1,i)
    
print(*answer)