#1620
import sys
n, m = map(int,sys.stdin.readline().strip().split())
poket_dict_num = dict()
poket_dict_name = dict()
for i in range(n):
    po = sys.stdin.readline().strip()
    poket_dict_name[i+1] = po
    poket_dict_num[po] = i+1
for i in range(m):
    poketmon = sys.stdin.readline().strip()
    if '0'<= poketmon[0] and '9'>= poketmon[0]:
        print(poket_dict_name[int(poketmon)])
    else:
        print(poket_dict_num[poketmon])