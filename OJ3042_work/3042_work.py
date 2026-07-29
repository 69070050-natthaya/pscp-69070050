"""หาร 10"""

n = int(input())
i = str(n)[-1]
zero = n - int(i)

while zero > -1:
    print(zero, end=" ")
    zero -= 10
