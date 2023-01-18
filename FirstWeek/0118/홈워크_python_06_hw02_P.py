# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 

words = ['eat','tea','tan','ate','nat','bat']
srtedwords = []
printwords = []
for i in range(len(words)) : 
    srtedwords += [sorted(words[i])]
for j in range(len(srtedwords)) :
    for k in range(j,len(srtedwords)) :
        if srtedwords[j] == srtedwords[k] :
            printwords += [words[k]]
        else :
            continue
dictwords = {words[i] : srtedwords[i] for i in range(len(words))}
valueList = list(dictwords.values())

lst1 = []
lst2 = []
lst3 = []
lstf = []

for i in words :
    if dictwords[i] == ['a', 'e', 't']:
        lst1.append(i)
    elif dictwords[i] == ['a', 'n', 't']:
        lst2.append(i)
    elif dictwords[i] == ['a', 'b', 't']:
        lst3.append(i)
lstf = [lst1] + [lst2] +[lst3]
print(lstf)


