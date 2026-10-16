"""as"""
lines = []
for _ in range(5):
    line = input().rstrip()
    lines.append(line)

if lines:
    max_length = 0
    for line in lines:
        if len(line) > max_length:
            max_length = len(line)
else:
    max_length = 0

top_last = "*" * (max_length + 4)
print(top_last)

for line in lines:
    padded_line = line.ljust(max_length)
    print("* " + padded_line + " *")

print(top_last)
