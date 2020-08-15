import math

def sockMerchant(n, ar):
    sock_count = {}
    num_pairs = 0
    for sock in ar:
        if sock not in sock_count:
            sock_count[sock]= 1
        else:
            sock_count[sock] += 1
    
    for key in sock_count:
        num_pairs += math.trunc(sock_count[key]/2)
    
    return num_pairs

n = 5
ar = [1,2,1,1,2]

print(sockMerchant(n,ar))