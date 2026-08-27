"""[LEARNING LOGS] สหกรณ์โรงเรียน"""
from decimal import Decimal, ROUND_HALF_UP

member = input().upper()
n = int(input())
total_price = Decimal("0")

for _ in range(1,n+1):
    price = Decimal(input())
    total_price += price

if member == "Y":
    total_price = total_price - (total_price * Decimal("5") / Decimal("100"))
elif member == "N" and total_price >= 500:
    total_price = total_price - (total_price * Decimal("3") / Decimal("100"))

#quantize คือ บอกว่าต้องการทศนิยมกี่ตำแหน่งเหมือนตัวนี้
rounded_total = total_price.quantize(Decimal("0.01"),ROUND_HALF_UP)
print(rounded_total)
