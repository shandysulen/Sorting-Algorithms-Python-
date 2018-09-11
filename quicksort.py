def quickSort(list):
    if len(list) <= 1:
        return list
    smaller = [x for x in list[1:] if x < list[0]]
    larger = [x for x in list[1:] if x >= list[0]]
    return quickSort(smaller) + [list[0]] + quickSort(larger)

# Main Function
if __name__ == '__main__':
    list = [2,4,5,1]
    print quickSort(list)
    
