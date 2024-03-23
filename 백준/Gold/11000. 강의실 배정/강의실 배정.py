#11000
import sys
import heapq
n = int(sys.stdin.readline())
lecture = []
for i in range(n):
  lecture.append(list(map(int,sys.stdin.readline().split())))
lecture.sort()
room = [lecture[0][1]]
for i in range(1,len(lecture)):
  if lecture[i][0] >= room[0]:
    heapq.heappop(room)
    heapq.heappush(room,lecture[i][1])
  else:
    heapq.heappush(room,lecture[i][1])
print(len(room))