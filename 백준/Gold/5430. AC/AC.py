t = int(input())
for _ in range(t):
    p = input()
    n = int(input())
    if n != 0:
        arr = list(map(int,input().replace("[","").replace("]","").split(',')))
    else:
        arr = input()
        arr = []
    reverse_flag = False
    start = 0
    last = len(arr)
    for c in p:
        if c == "R":
            if reverse_flag == True:
                reverse_flag = False
            else:
                reverse_flag = True
        if c == "D":
            if start>= last:
                arr = "error"
                break
            if reverse_flag == False:
                start += 1
            else:
                last -= 1
    if arr != "error":
        arr = arr[start:last]
        if reverse_flag:
            arr.reverse()
    print(str(arr).replace(" ",""))