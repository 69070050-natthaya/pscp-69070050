"""แปลงดอกไม้"""

line , n =map(int , input().split())
i = 1
count = 0
answer = 0
if line != 1:
    first = n // line
    second = first % line
    answer = first // line
    if not second:
        answer = answer
    else:
        answer = answer + 1
    print(answer)
else:
    while i <= n:
        n = n - i
        i += 1
        count += 1
    if n > 0:
        count = count + 1
    print(count)
