infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]
hap = 0
for i in range(len(infos)) :
    hap += infos[i]['age']
print(hap)