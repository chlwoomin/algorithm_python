from queue import PriorityQueue
N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
pq = PriorityQueue()
for meeting in meetings:
    pq.put(meeting)
current_meeting = [0,0]
res = []
while not pq.empty():
    meeting = pq.get()
    if meeting[0] < current_meeting[1]:
        if meeting[1] < current_meeting[1]:
            res.pop()
        else:
            continue
    current_meeting = meeting
    res.append(current_meeting)
print(len(res))