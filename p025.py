a, b, count = 1, 1, 2

while 1:
    c = b
    b += a
    a = c
    count += 1
    if len([_ for _ in str(b)]) == 1000:
        print(count)
        break


