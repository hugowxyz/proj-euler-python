import math

def abundant(n):
    _sum = 1
    for i in range(math.floor(math.sqrt(n)), 1, -1):
        if n % i == 0:
            if n/i != i:
                _sum += i + n/i
            else:
                _sum += i

        if _sum > n:
            return True

    return False

file = open("p023.txt", "w")

for i in range(4, 28123):
    if abundant(i):
        file.write(str(i) + ' ')

file.close()

file0 = open("p023.txt", "r")

data = file0.readlines()[0].split(" ")

file0.close()

del data[-1]

file1 = open("p023_2.txt", "w")

c = 0
p = {}

for i in range(len(data)):
    for j in range(i, len(data)):
        a, b = int(data[i]), int(data[j])
        if a + b <= 28123 and a + b not in p:
            file1.write(str(a+b) + ' ')
            p[a+b]=1
    c += 1
    if c % 100 == 0: print(c, end=" ")

file1.close()

file = open("p023_2.txt", "r")
data = file.readlines()[0].split(" ")

print(data[-1])

del data[-1]

ans = 0

for i in data:
    ans += int(i)

print(1/2 * 28123 * 28124 - ans)

file.close()
