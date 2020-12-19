import math, time

start = time.time()

def prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)+1), 2):
        if n % i == 0:
            return False
    return True

primes = {}
_max = 0
answer = 0

for b in range(2, 1000):
    if prime(b):
        primes[b] = 1
        
        for a in range(-999, 1000, 2):
            n, count = 0, 0
            while True:
                if n**2 + a * n + b in primes:
                    count += 1
                else:
                    if count > _max:
                        answer = a * b
                        _max = count
                    break
                n+=1

print(answer)
end = time.time()

print(end-start)
        
