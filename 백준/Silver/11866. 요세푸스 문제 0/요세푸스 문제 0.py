#11866
n, k = map(int,input().split())
kk = k
queue = [i+1 for i in range(n)]
answer = []
while len(queue)>0:
    try:
        answer.append(queue.pop(kk-1))
        kk= kk + k-1
        if kk > len(queue):
            kk -= len(queue)
    except:
        if kk > len(queue):
            kk -= len(queue)
print('<' + str(answer).strip("[""]") + '>')