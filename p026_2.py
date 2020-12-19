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
        print(count)
        return True
            
    return False
        

def rl(digits):
    tried = {}
    for a in digits:
        for i in range(1, len(digits[a])):
            for j in range(i):
                length = digits[a][i] - digits[a][j]
                if length not in tried:
                    #print(length, end=" ")
                    if try_guess(digits, length):
                        return length
                tried[length] = 1
    return 0
