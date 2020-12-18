#Recursive algorithm for generating permutations
chosen = {key:False for key in range(10)}
permutation = []
n, count = 10, 0

def generate():
    global permutations, chosen, permutation, n, count

    if len(permutation) == n:
        count += 1
        
    if count == 1000000:
        print(permutation)
        return
    
    else:
        for i in range(n):
            if chosen[i]: continue
            chosen[i] = True
            permutation.append(i)
            generate()
            chosen[i] = False
            permutation.pop()

generate()
            
