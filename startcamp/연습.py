min_num, max_num = map(int, input().split())
numlist = []
multiResult = min_num
while max_num >= multiResult :
    numlist.append(multiResult)
    multiResult += min_num

arr = [i for _ in range(numlist[0],numlist[-1])]