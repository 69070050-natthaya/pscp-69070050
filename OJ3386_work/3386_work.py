"""Duplicate I"""

m = int(input())
n = int(input())

g1 = set()
for _ in range(m):
    g1.add(input().strip())

g2 = set()
for _ in range(n):
    g2.add(input().strip())

common = g1 & g2

if not common:
    print("Nope")
else:
    for s in sorted(common, key=int, reverse=True):
        print(s)
