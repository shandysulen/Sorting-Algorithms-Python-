def insertionSort(A):
    for j in range(1, len(A)):
        i = j - 1
        key = A[j]
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]             
            i -= 1            
        A[i + 1] = key
    return A

def decreaseInsertionSort(A):
    for j in range(1, len(A)):
        i = j - 1
        key = A[j]
        while i >= 0 and A[i] < key:
            A[i + 1] = A[i]             
            i -= 1            
        A[i + 1] = key
    return A

# print(insertionSort([3,1,2,4,5,6,8,5,2]))
print(insertionSort([31,41,59,26,41,58]))
print(decreaseInsertionSort([31,41,59,26,41,58]))