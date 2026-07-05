"""Elo"""

RA = int(input())
RB = int(input())
A = input()

EA = 1 / (1 + (10**((RB-RA)/400)))
EB = 1 / (1 + (10**((RA-RB)/400)))

if A == "A":
    print(f"{EA:.2f}")
elif A == "B":
    print(f"{EB:.2f}")
