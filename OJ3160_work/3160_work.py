"""[LEARNING LOGS] หาจำนวนเฉพาะ"""

start,stop = input().split()
start = int(start)
stop = int(stop)
prime = []
before_answer = 0
answer = 0

for num in range(start,stop + 1):
    if num == 1 or not num:
        is_prime = False
    else:
        is_prime = True

    for i in range(2 , num):
        if not num % i:
            is_prime = False
            break

    if is_prime:
        prime.append(num)

before_answer = " ".join(map(str,prime))
answer = len(prime)

if not answer:
    print(f"Total primes: {answer}")
else:
    print(before_answer)
    print(f"Total primes: {answer}")
