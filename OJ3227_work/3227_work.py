"""[LEARNING LOGS] ไพ่ 44 ใบ"""
card = list(input().lower())
group = ""
score = ""

if card[-1] == "d":
    group = "diamonds"
elif card[-1] == "h":
    group = "hearts"
elif card[-1] == "s":
    group = "spades"
elif card[-1] == "c":
    group = "clubs"

if card[-2] == "a":
    score = "ace"
elif card[-2] == "2":
    score = "2"
elif card[-2] == "3":
    score = "3"
elif card[-2] == "4":
    score = "4"
elif card[-2] == "5":
    score = "5"
elif card[-2] == "6":
    score = "6"
elif card[-2] == "7":
    score = "7"
elif card[-2] == "8":
    score = "8"
elif card[-2] == "9":
    score = "9"
elif card[-2] == "0":
    score = "10"
elif card[-2] == "j":
    score = "jack"
elif card[-2] == "q":
    score = "queen"
elif card[-2] == "k":
    score = "king"

print(f"{score} of {group}")
