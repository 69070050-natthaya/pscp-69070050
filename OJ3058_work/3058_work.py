"""BrickBridge"""

a = int(input())
b = int(input())
goal = int(input())
x = 0
big = b * 5
if big >= goal :
    x = goal // 5
else :
    x = b
if goal - (x * 5) <= a :
    print(goal - (x * 5))
else :
    print("-1")
