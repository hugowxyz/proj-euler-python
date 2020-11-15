ans = 1
for i in range(1, 101):
    ans *= i
ans1 = 0
for i in str(ans):
    ans1 += int(i)
print(ans1)
