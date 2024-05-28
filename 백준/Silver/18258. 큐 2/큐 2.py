#18258
import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque()
for i in range(n):
    command = list(sys.stdin.readline().split())
    try:
        if command[0] == 'push':
            queue.append(command[1])
        elif command[0] == 'pop':
            print(queue.popleft())
        elif command[0] == 'size':
            print(len(queue))
        elif command[0] == 'empty':
            if len(queue) == 0:
                print(1)
            else:
                print(0)
        elif command[0] == 'front':
            print(queue[0])
        elif command[0] == 'back':
            print(queue[len(queue)-1])
    except:
        print(-1)
    