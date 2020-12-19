def gcf(a, b):
    if (b==0): return a
    return gcf(b,a%b)

max_ = -1

for i in range(1,10**6):
    tot = 0
    for j in range(1, i+1):
        if tot > (i/max_):
            tot = 999999
            break
        if gcf(i, j) == 1:
            tot += 1
    if i/tot > max_:
        max_ = i/tot
        ans = i

print(ans)
