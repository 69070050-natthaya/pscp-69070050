"""Season"""

month = int(input())
day = int(input())

if month in {1,2}:
    print("winter")
elif month == 3 and day <= 20:
    print("winter")
elif month == 3 and day >= 21:
    print("spring")
elif month in {4,5}:
    print("spring")
elif month == 6 and day <= 20:
    print("spring")
elif month == 6 and day >= 21:
    print("summer")
elif month in {7,8}:
    print("summer")
elif month == 9 and day <= 20:
    print("summer")
elif month == 9 and day >= 21:
    print("fall")
elif month in {10,11}:
    print("fall")
elif month == 12 and day <= 20:
    print("fall")
elif month == 12 and day >= 21:
    print("winter")
