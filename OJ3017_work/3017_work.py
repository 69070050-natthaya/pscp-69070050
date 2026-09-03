"""Bill"""

price = int(input())
ser = price * 10/100

if ser < 50:
    ser = 50
elif ser > 1000:
    ser = 1000

price_ser = price + ser

vat = price_ser * 7/100

total = price_ser + vat

print(f"{total:.2f}")
