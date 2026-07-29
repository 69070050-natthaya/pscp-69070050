"""หาจำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""

first_number = int(input())
last_number = int(input())
d = int(input())
r = int(input())

answer = 0
for i in range(first_number,last_number + 1):
    if i % d == r:
        answer += 1

print(answer)
