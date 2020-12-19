def divide(a, b):
    digits = []
    c = a
    for i in range(2000):
        c = c%b * 10

        digits.append(str(c//b))

        if c%b == 0:
            return digits
        c = c % b
    return digits

def show(d, n):
    print("".join(divide(1,d)[0:n]))
    
for i in range(100, 200):
    print(1/i)
