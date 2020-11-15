def d(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s+=i
    return s

amicable = []
for i in range(2, 10000+1):
    if i == d(d(i)) and i != d(i):
        amicable.append(i)

print(sum(amicable))
