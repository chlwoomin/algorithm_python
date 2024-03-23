#7568
n = int(input())
people = []
rank = [1] * n
for i in range(n):
    people.append(list(map(int, input().split())))

for compare_people1 in range(n):
    for compare_people2 in range(n):
        if compare_people1 == compare_people2:
            continue
        if people[compare_people1][0] < people[compare_people2][0] and people[compare_people1][1] < people[compare_people2][1]:
            rank[compare_people1]+=1
print(*rank)