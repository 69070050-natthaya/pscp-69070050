"""isPrime_large"""

def is_prime(num):
    """Doc"""
    if num < 2:
        return False
    if num == 2:
        return True
    if not num % 2:
        return False
    i = 3
    while i * i <= num:
        if not num % i:
            return False
        i += 2
    return True


n = int(input())
print("YES" if is_prime(n) else "NO")
