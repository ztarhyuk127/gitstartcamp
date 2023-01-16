score = {
    'python': 85,
    'django': 89,
    'web': 83,
    'algorithm' : 90
}
hap = 0
scoreKeyList = list(score.keys())
scoreValueList = list(score.values())

for i in range(len(scoreValueList)):
    hap += scoreValueList[i]
print(hap / len(scoreKeyList))

