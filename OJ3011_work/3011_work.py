"""Colors"""

c1 = input().strip().lower()
c2 = input().strip().lower()

if c1 not in ["red", "yellow", "blue"] or c2 not in ["red", "yellow", "blue"]:
    print("Error")
elif c1 == c2:
    print(c1.capitalize())
elif (c1 == "red" and c2 == "yellow") or (c1 == "yellow" and c2 == "red"):
    print("Orange")
elif (c1 == "red" and c2 == "blue") or (c1 == "blue" and c2 == "red"):
    print("Violet")
elif (c1 == "yellow" and c2 == "blue") or (c1 == "blue" and c2 == "yellow"):
    print("Green")
