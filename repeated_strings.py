import re
import math

def repeatedString(s ,n):
    count = s.count('a')
    
    #y gives the number of times s will fit into n and drops the remainder
    y = n//len(s)

    #z slices the remainder of n up and counts the rest of the a's
    z = s[0:(n-len(s)*y)].count('a')

    #muliply how many a's are in s by the number of times s fits into n and then add any stragglers.
    count = count * y + z

    #Woo-hoo!
    return count

s='aba'
print(repeatedString(s, 10))