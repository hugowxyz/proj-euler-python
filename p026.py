##def find(array, n):
##    for i in range(len(array)):
##        if array[i] == n:
##            return i
##    return -1

##def rl(array):
##    for i in range(1, len(array)):
##        index = find(array, array[i])
##        if index >= 0 and index != i:
##            if "".join(array[index:i]) == "".join(array[i:i+i-index]):
##                return i-index
##    return 0

##def rl(digits):
##    tried = {}
##    best = -1
##    for a in digits:
##        for i in range(len(digits[a])):
##            for j in range(i):
##                flag = True
##                if best > 0:
##                    length = best
##                else:
##                    length = digits[a][i]-digits[a][j]
##                    
##                if length in tried:
##                    break
##                tried[length]=1
##
##                for k in range(2, int(digits[a][-1]/length)):
##                    if digits[a][0] + k * length not in digits[a]:
##                        flag = False
##                        best = -1
##                        break
##
##                if flag:
##                    best = length
##                    break
##    return best

def divide(a, b):
    digits = {}
    c = a
    index=0
    for i in range(2000):
        c = c%b * 10

        if str(c//b) not in digits: digits[str(c//b)] = [index]
        else: digits[str(c//b)].append(index)

        if c%b == 0:
            return digits
        c = c % b
        index+=1
    return digits

# Check that the length is valid for each key
# Starting from any index for at least 5 digits
# Is it sufficient that only 1 digit holds this property?

def try_guess(digits, length):
    for a in digits:
        for j in range(0, len(digits[a])):
            flag = True
            for k in range(2, 6):
                if digits[a][j] + k * length not in digits[a]:
                    flag = False
                    break
            if flag:
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

    for d in range(2, 1000):
        length = rl(divide(1, d))
        if d % 100 == 0:
            print(d, end=" ")
        if length > biggest:
            biggest = length
            ans = d

    print(ans, biggest)


#main()

for i in range(2, 1000):
    print(1/i)
