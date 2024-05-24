#28278
import heapq
import sys
n = int(sys.stdin.readline())
stack = []
for i in range(n):
    command = list(map(int,sys.stdin.readline().split()))
    try :
        if command[0] == 1:
            stack.append(command[1])
        elif command[0] == 2:
            print(stack.pop())
        elif command[0] == 3:
            print(len(stack))
        elif command[0] == 4:
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        else:
            print(stack[len(stack)-1])
    except:
        print(-1)
