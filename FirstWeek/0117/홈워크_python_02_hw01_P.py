orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
lst = []
i = 0
print(len(orders))
while orders[i] != orders[len(orders)-1] :  
    for j in range(len(orders)):
        if orders[j] == ',' :
            lst.append(orders[i:j])
            j+= 1
            i = j
            continue
        if j == len(orders):
            lst.append(orders[i:j])
    break


