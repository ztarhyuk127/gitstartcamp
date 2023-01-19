def dict_list_sum(a) :
    hap = 0
    for i in range(len(a)) :
        hap += a[i]['age']
    return hap
print(dict_list_sum([{'name':'kim','age':12},{'name':'lee','age':4}])) 