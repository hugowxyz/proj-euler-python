import time

def divide(a, b):
    digits = {}
    c = a
    index=0
    for i in range(5000):
        c = c%b * 10

        if str(c//b) not in digits: digits[str(c//b)] = [index]
        else: digits[str(c//b)].append(index)

        if c%b == 0:
            return digits
        c = c % b
        index+=1
    return digits

def try_guess(digits, length):
    count = 0
    for a in digits:
        for j in range(0, int(len(digits[a])/100)):
            flag = True
            for k in range(1, 6):
                if digits[a][j] + k * length not in digits[a]:
                    flag = False
                    break
            if flag:
                count += 1

    if count >= int(len(digits.keys())/3):
        return True
            
    return False
        

def rl(digits):
    tried = {}
    for a in digits:
        for i in range(1, len(digits[a])):
            for j in range(i):
                length = digits[a][i] - digits[a][j]
                if length not in tried:
                    if try_guess(digits, length):
                        return length
                tried[length] = 1
    return 0


def main():
    biggest, ans = 0, 0

    for d in range(3, 1000, 2):
        length = rl(divide(1, d))
        if d % 99 == 0: print(d, end=" ")
        if length > biggest:
            biggest = length
            ans = d

    print(ans, biggest)

start = time.time()
main()
end = time.time()
print(end - start)

# Roughly 14.45 seconds
# 983 with cycle length 982
