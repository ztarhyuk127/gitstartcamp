n = 13521
list1 = []
list2 = []
hap = 0
n = str(n)
for i in range(len(n)):
    list1 += n[i]

print(list1)

for j in list1:
    list2+=[int(j)]
for k in range(list2) :
    factorhap = list2[k] * (10 ** (len(list2)-(k+1))) + list2[k]
    hap += factorhap
print(hap)


