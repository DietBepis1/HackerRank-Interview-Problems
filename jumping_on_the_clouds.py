def jumpingOnClouds(c):
    loc = 0
    num_jumps = 0

    while loc < len(c)-1:
        if (loc+2 < len(c)) and (c[loc+2] != 1):
            print('2 steps', f'{c[loc]}')
            loc += 2
            num_jumps += 1 
        else:
            print('1 steps', f'{c[loc]}')
            loc += 1
            num_jumps += 1
    
    return num_jumps

c = [0,1,0,0,1,0]
print(jumpingOnClouds(c))