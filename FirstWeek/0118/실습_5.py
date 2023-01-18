import sys

wtrhap = 0
slthap = 0
T = int(input())
for TestCase in range(1,1+T) :
    nong, yang = sys.stdin.readline().rstrip().split(' ')
    if nong[-1] == '%':
        nong = nong[:-1]
    nong = (float(nong))/100
    yang = float(yang)
    sltyang = yang * nong
    wtrhap +=yang
    slthap +=sltyang
mixed_nongdo = (slthap / wtrhap) * 100
DoneAtLast = input()
if DoneAtLast == 'Done' :
    print(f"{round(mixed_nongdo,2)}% , {round(wtrhap,2)}")

