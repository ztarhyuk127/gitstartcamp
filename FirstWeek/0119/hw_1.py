# 1. 제네레이터 정의 101 = 9 + 1 + 91 >> 101의 제네레이터 = 91 or 101
# 2. 제네레이터가 없는 셀프넘버를 판별하는 함수
n = int(input())
def fn_d(n) :
    binliststr = []
    binlistint = []
    strn = str(n)
    hap = 0
    for i in range(len(strn)):
        binliststr +=strn[i]
    binliststr += [strn]
    for j in binliststr :
       binlistint += [int(j)]
    
    for k in binlistint :
        hap += k
    return hap

def is_selfnumber(n):
    numbers = list(range(1, n+1))
    remove_list = []
    self_list=[]
    for num in numbers :
        for n in str(num):
            num += int(n) 
        if num <= n:  
            remove_list.append(num)  

    for remove_num in set(remove_list) : 
        numbers.remove(remove_num)
    for self_num in numbers :  
        self_list += [self_num]
    if n in self_list :
        return True
    else :
        return False
is_selfnumber(fn_d(n))

        
