"""[LEARNING LOGS] RGB Mixed"""

r1 , g1 , b1 = input().split()
r2 , g2 , b2 = input().split()
r = (int(r1) + int(r2)) // 2
g = (int(g1) + int(g2)) // 2
b = (int(b1) + int(b2)) // 2

print(r , g , b , sep=" ")
