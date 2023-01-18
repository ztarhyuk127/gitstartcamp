orders = ['아이스아메리카노','카라멜마키야또','에스프레소','아메리카노','아메리카노','아이스라떼','핫초코','아이스아메리카노','아메리카노','아이스카라멜마키야또','아이스라떼','라떼마키야또','카푸치노','라떼마키야또']

order_dict = {}
for order in orders :
    if order in order_dict:
        order_dict[order] += 1
    else :
        order_dict[order] = 1