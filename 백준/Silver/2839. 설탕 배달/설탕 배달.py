n = int(input())
answer = 0
for cnt5 in range((n//5), -1 , -1):
    sum1 = n - (cnt5*5)
    if sum1 % 3 == 0:
        answer = sum1//3 + cnt5
        break
if answer == 0:
    print(-1)
else:
    print(answer)