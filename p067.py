file = open("p067_triangle.txt", "r")
array = [_.strip("\n").split(" ") for _ in file.readlines()]
mem = dict()

def recursion(x, y):
    global mem
    
    if y == len(array)-1 or (y == len(array)-1 and x == len(array[y]-1)):
        return int(array[y][x])

    if f"{x},{y+1}" in mem and f"{x+1},{y+1}" in mem:
        optimal = max(mem[f"{x},{y+1}"], mem[f"{x+1},{y+1}"])
    else:
        optimal = max(recursion(x, y+1),
                   recursion(x+1, y+1))

    mem[f"{x},{y}"] = int(array[y][x]) + optimal

    return mem[f"{x},{y}"]

def main():
    recursion(0, 0)
    print(mem["0,0"])
    
main()
