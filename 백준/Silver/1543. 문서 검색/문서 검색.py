document = input()
word = input()
cnt = 0
i=0
while i<len(document):
    if document[i:i+len(word)] == word:
        cnt += 1
        i += len(word)
        continue
    i+=1

print(cnt)