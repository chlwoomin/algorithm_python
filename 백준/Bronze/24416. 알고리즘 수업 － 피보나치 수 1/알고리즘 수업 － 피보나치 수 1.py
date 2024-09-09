#24416
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
def fibo(n):
    f = [0]*n
    for i in range(2,n):
        f[i] = f[i-1] + f[i-2]
    return n-2
n = int(input())
print(fib(n),fibo(n))