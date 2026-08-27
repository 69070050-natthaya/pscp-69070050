"""[LEARNING LOGS] สงคราม...ส่งด่วน"""

first,last = input().upper().split()
weigth = float(input())
fee = 0
weigth_fee = 0

if first == "BKK" and last == "CNX":
    fee = 10
    weigth_fee = 30 * weigth
    print(f"{fee + weigth_fee:.2f}")
elif first == "CNX" and last == "UBP":
    fee = 15
    weigth_fee = 40 * weigth
    print(f"{fee + weigth_fee:.2f}")
elif first == "UBP" and last == "BKK":
    fee = 20
    weigth_fee = 40 * weigth
    print(f"{fee + weigth_fee:.2f}")
elif first == "BKK" and last == "PKT":
    fee = 25
    weigth_fee = 50 * weigth
    print(f"{fee + weigth_fee:.2f}")
elif first == "PKT" and last == "CNX":
    fee = 30
    weigth_fee = 60 * weigth
    print(f"{fee + weigth_fee:.2f}")
elif first == "UBP" and last == "PKT":
    fee = 40
    weigth_fee = 70 * weigth
    print(f"{fee + weigth_fee:.2f}")
else:
    print("Error")
