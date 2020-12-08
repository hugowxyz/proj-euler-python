file = open("p022_names.txt", "r")
array = [_.replace("\"", "") for _ in file.read().split(",")]
array.sort()
alphabet = [chr(letter) for letter in range(ord('A'), ord('Z')+1)]

ans = 0

for i in range(len(array)):
    s = 0
    for j in array[i]:
        s += alphabet.index(j) + 1
    ans += (s * (i+1))

print(ans)
