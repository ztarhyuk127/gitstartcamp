orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
lst = []
icelst = []
i = 0
while True :  
    for j in range(len(orders)):
        if orders[j] == ',' or j == len(orders)-1:
            j+= 1
            lst.append(orders[i:j])
            i = j
            continue
    if orders[i-1] == orders[len(orders)-1] :
        break
for ice in range(len(lst)) :
    if '아이스' in lst[ice] :
        icelst.append(lst[ice])
print(f"아이스 메뉴 주문 수 : {len(icelst)}")

jungbok = 0
for num1 in range(len(lst)) :
    for num2 in range(num1+1,len(lst)):
        if lst[num1] == lst[num2] :
            jungbok += 1
        value = jungbok
    jungbok =0
    dictorder = {final : value for final in lst}
print(dictorder)