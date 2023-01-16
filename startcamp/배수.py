T = int(input())
for TestCase in range(1, 1+T):
    min_num, max_num = map(int, input().split())
    numlist = []
    multiResult = min_num
    numlist.append(f"#{TestCase}")
    while max_num >= multiResult :
        numlist.append(multiResult)
        multiResult += min_num
    for i in range(0,len(numlist)) :
        print(f"{numlist[i]}",end =' ')
    print()
