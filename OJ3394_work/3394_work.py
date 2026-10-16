"""ส่งต่อ"""

data = []
try:
    while True:
        data += input().split()
except EOFError:
    pass

n, s = int(data[0]), int(data[1])
nxt = [0] * (n + 1)
for i in range(1, n + 1):
    nxt[i] = int(data[1 + i])

visited = [False] * (n + 1)
cur = s
count = 0
while cur and not visited[cur]:
    visited[cur] = True
    count += 1
    cur = nxt[cur]

print(count)
