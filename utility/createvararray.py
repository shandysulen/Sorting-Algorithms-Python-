import random

def createArrayAndTarget(length, lower_bound, higher_bound):    
    A = [random.randint(lower_bound, higher_bound) for x in range(length)]  
    target = A[random.randint(0, length - 1)]
    return (A, target)

