"""[LEARNING LOGS] เกมสะสมแต้ม"""

n = int(input())
count = 0
score = 0

while count < n:
    x = input()
    if x == "+":
        score += 10
    elif x == "-":
        score -= 5
    count += 1

print(score)
