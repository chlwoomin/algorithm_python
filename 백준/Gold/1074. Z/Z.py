def div(N, r, c):
    global res
    if N == 0:
        return
    middle = 2**(N-1) - 1

    if middle>= r:
        if middle>= c:
            div(N-1, r, c)
        else:
            res += 4**(N-1)
            div(N-1, r, c - (middle + 1))
    else:
        if middle>= c:
            res += 4**(N-1) * 2
            div(N-1, r - (middle + 1), c)
        else:
            res += 4**(N-1) * 3
            div(N-1, r - (middle + 1), c - (middle + 1))

N, r, c = map(int, input().split())
res = 0
div(N, r, c)
print(res)