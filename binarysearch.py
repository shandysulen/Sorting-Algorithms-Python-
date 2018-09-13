def binarySearch(A, left, right, target):
    if right >= 1:
        mid = left + (right-left) // 2
        print(f"Mid: {mid}")
        if A[mid] == target:
            return mid
        elif A[mid] < target:
            return binarySearch(A, mid + 1, right, target)
        elif A[mid] > target:        
            return binarySearch(A, left, mid - 1, target)
    else:
        return -1
        
