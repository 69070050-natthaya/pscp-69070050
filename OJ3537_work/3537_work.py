"""Impostor"""

import ast

players = {}

while True:
    line = input().strip()
    if line == "Start":
        break
    players.update(ast.literal_eval(line))

dead = {}
while True:
    name = input().strip()
    if name == "End":
        break
    if name in players:
        dead[name] = players.pop(name)

impostor_left = list(players.values()).count("Impostor")

print(impostor_left, "Impostor Remains")

print("***Alive***")
for name in sorted(players):
    print(name, ":" , players[name])

print("***Dead***")
for name in sorted(dead):
    print(name, ":" , dead[name])
