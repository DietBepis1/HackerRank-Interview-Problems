import math

def countingValleys(n, s):
    count = 0
    num_valleys = 0
    for letter in s[0::1]:
        if letter == 'D' or letter == 'd':
            if count == 0:
                num_valleys += 1
            count -= 1
        elif letter == 'U' or letter == 'u':
            count +=1
            
    return num_valleys

s = 'UDDDUDUU'
print(countingValleys(5, s))