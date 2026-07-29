"""หาว่ามีสระกี่ตัว"""

word = input().lower()
a = word.count("a")
e = word.count("e")
i = word.count("i")
o = word.count("o")
u = word.count("u")

if "a" in word:
    print(f"a : {a}")

if "e" in word:
    print(f"e : {e}")

if "i" in word:
    print(f"i : {i}")

if "o" in word:
    print(f"o : {o}")

if "u" in word:
    print(f"u : {u}")
