def list_sum(a):
    hap = 0
    for i in range(len(a)) :
        hap += a[i]
    return hap

print(list_sum([1,2,3,4,5]))