#11478
s = input()
answer = set()
for i in range(len(s)):
    for j in range(len(s)-i):
        answer.add(s[j:(j+i)+1])
print(len(answer))