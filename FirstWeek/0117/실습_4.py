# 출력 결과 예시
# 스테이크   50,000
# + VAT     7,500
# 총계 ₩    57,500

steak_price = 50000
vat = int(50000 * 0.15)
total_price = round((1 + 0.15) * steak_price)

print(f"스테이크  {steak_price}")
print(f"+ VAT     {vat}")
print(f"총계 ₩    {total_price}")
