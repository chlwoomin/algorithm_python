#28279
import sys
from collections import deque
d = deque()
n = int(input())
for i in range(n):
    command = sys.stdin.readline().split()
    try:
        if command[0] == '1':
            d.appendleft(command[1])
        elif command[0] == '2':
            d.append(command[1])
        elif command[0] == '3':
            print(d.popleft())
        elif command[0] == '4':
            print(d.pop())
        elif command[0] == '5':
            print(len(d))
        elif command[0] == '6':    
            if len(d) == 0:
                print(1)
            else:
                print(0)    
        elif command[0] == '7':
            print(d[0])
        elif command[0] == '8':
            print(d[len(d)-1])
    except:
        print(-1)