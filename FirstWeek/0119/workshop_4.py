def all_list_sum(a) :
    hap = 0
    for i in range(len(a)) :
        for j in range(len(a[i])) :
            hap += a[i][j]
    return hap

print(all_list_sum([[1],[2,3],[4,5,6],[7,8,9,10]]))