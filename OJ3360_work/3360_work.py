"""หั่นขนมปัง"""

w , h , _ , _ = map(int, input().split())
xs = list(map(int, input().split()))
ys = list(map(int, input().split()))

px = [0] + xs + [w]
py = [0] + ys + [h]
ws = sorted((px[i + 1] - px[i] for i in range(len(px) - 1)), reverse=True)
hs = sorted((py[i + 1] - py[i] for i in range(len(py) - 1)), reverse=True)

first = ws[0] * hs[0]
second = max(ws[0] * hs[1], ws[1] * hs[0])
print(first, second)
