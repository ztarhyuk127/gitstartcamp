import sys
N = int(input())
scoreList = list(map(int,sys.stdin.readline().rstrip().split()))
if len(scoreList) == N :
    scoreList.sort()
    M = scoreList[-1]
    newscoreList = [scoreList[i]/M * 100 for i in range(N)]
    newHap = 0
    for i in newscoreList :
        newHap += i
        newAve = newHap / N
    print(newAve)
