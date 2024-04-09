#7785
import sys
n = int(sys.stdin.readline())
a_dict = dict()
for i in range(n):
    key,value = map(str,sys.stdin.readline().split())
    if value == 'enter':
        a_dict[key] = value
    elif value == 'leave':
        del a_dict[key]
a_dict = sorted(a_dict,reverse=True)
for i in a_dict:
    print(i)