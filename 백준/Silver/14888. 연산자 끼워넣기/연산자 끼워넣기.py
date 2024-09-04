#14888        
def dfs(n, num, plus,minus,mul,div):
    global maximum,minimum
    if plus + minus + mul + div == 0:
        maximum = max(maximum,num)
        minimum = min(minimum,num)
        return
    if plus > 0:
        dfs(n+1,num + number[n],plus-1,minus,mul,div)
    if minus > 0:    
        dfs(n+1,num - number[n],plus,minus-1,mul,div)
    if mul > 0:
        dfs(n+1,num * number[n],plus,minus,mul-1,div)
    if div > 0:
        if num < 0:
            num = num * -1
            dfs(n+1,-(num // number[n]),plus,minus,mul,div-1)
        else:
            dfs(n+1,num // number[n],plus,minus,mul,div-1)
    
maximum = -1000000000
minimum = 1000000000
n = int(input())
number = list(map(int,input().split()))
plus, minus, mul, div = map(int,input().split())
dfs(1,number[0],plus,minus,mul,div)
print(maximum)
print(minimum) 