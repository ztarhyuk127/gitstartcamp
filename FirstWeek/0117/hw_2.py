# 1. 아이스 음료 주문 수
# 2. 메뉴 별 주문 수.

orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
orders = orders.split(',') # 개떡같은 문자열을 단번에 리스트화!
icecnt = 0
for i in orders:
    if '아이스' in i :
        icecnt += 1
print(f"아이스 음료 {icecnt}잔 주문함")
order_dict = {}

for j in orders:
    # order => key로 사용
    # order_dict[order] = order_dict.get(order, 0) + 1
    if j in order_dict:
        order_dict[j] = order_dict[j] + 1
    else:
        order_dict[j] = 1
print(order_dict)