def radixSort(A):
    m = max(A)
    exp = 1
    while m/exp > 0:
        countSort(A, exp)
        exp *= 10
    # return ___

def countSort(A, exp):
    n = len(A)

    output = [0] * (n)
    count = [0] * (10)

    for i in range(0, n):
        index = A[i] / exp
        count[ int(index % 10) ] += 1
    
    for i in range(1,10):
        count[i] += count[i-1]
    
    i = n - 1
    while i >= 0:
        index = (A[i]/exp)
        output[ count[int(index % 10) ] - 1] = A[i]
        count[ int(index % 10)] -= 1
        i -= 1

    i = 0
    for i in range(0, len(A)):
        A[i] = output[i]

A = [ 170, 45, 75, 90, 802, 24, 2, 66]
radixSort(A)

for i in range(len(A)):
    print(A[i])

