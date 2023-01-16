# 문제풀이

twolist = list(range(2,1000,2))
sevlist = list(range(7,1000,7))
set_all = set(twolist + sevlist)
again_list = list(set_all)
hap = 0

for i in range(len(again_list)):
    hap += again_list[i]
print(hap)