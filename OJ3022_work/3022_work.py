"""Temperature"""

temp = float(input())
first = input().upper()
last = input().upper()

if first == "C":
    if last == "K":
        print(f"{temp + 273.15:.2f}")
    elif last == "F":
        print(f"{temp * 9 / 5 + 32:.2f}")
    elif last == "R":
        print(f"{(temp + 273.15) * 9 / 5:.2f}")
    elif last == "C":
        print(temp)
elif first == "K":
    temp_c = temp - 273.15
    if last == "C":
        print(f"{temp_c:.2f}")
    elif last == "F":
        print(f"{temp_c * 9 / 5 + 32:.2f}")
    elif last == "R":
        print(f"{(temp_c + 273.15) * 9 / 5:.2f}")
    elif last == "K":
        print(temp)
elif first == "F":
    temp_c = (temp - 32) * 5 / 9
    if last == "C":
        print(f"{temp_c:.2f}")
    elif last == "K":
        print(f"{temp_c + 273.15:.2f}")
    elif last == "R":
        print(f"{(temp_c + 273.15) * 9 / 5:.2f}")
    elif last == "F":
        print(temp)
elif first == "R":
    temp_c = (temp * 5 / 9) - 273.15
    if last == "C":
        print(f"{temp_c:.2f}")
    elif last == "K":
        print(f"{temp_c + 273.15:.2f}")
    elif last == "F":
        print(f"{temp_c * 9 / 5 + 32:.2f}")
    elif last == "R":
        print(temp)
