"""Giraffe"""

n = int(input())
all_high = []

for _ in range(1,n+1):
    high = int(input())
    all_high.append(high)

count = 0
for i in range(n):
    left = (not i) or (all_high[i] > all_high[i - 1])
    right = (i == n - 1) or (all_high[i] > all_high[i + 1])
    if left and right:
        count += 1

print(count)
