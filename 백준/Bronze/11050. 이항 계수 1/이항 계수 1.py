#11050
def pac(n):
    pacto = 1
    for i in range(n):
        pacto = pacto*(i+1)
    return pacto
    
n,k = map(int,input().split())
print(int(pac(n)/pac(n-k)/pac(k)))