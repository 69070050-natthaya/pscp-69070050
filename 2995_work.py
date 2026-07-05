"""การตรวจสอบบัตรนักศึกษา"""
ID = input()

if len(ID) == 8:
    if ID[2] == "1" and ID[3] == "6":
        print("yes")
    else:
        print("no")
else:
    print("no")
