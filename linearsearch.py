def linearSearch(A, target):    
    for i in range(len(A)):
        if A[i] == target:            
            return i
    return -1

def linearSentinelSearch(A, target):    
    A.append(target)
    i = 0

    while True:
        if A[i] == target:
            if i < len(A):                
                return i
            else:                
                return -1
        i += 1
