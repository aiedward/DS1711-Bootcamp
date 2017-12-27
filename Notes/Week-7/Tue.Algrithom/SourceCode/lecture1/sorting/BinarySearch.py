def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
 
    while first <= last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    
    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 32))






def binarySearchRecursive(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
                return binarySearchRecursive(alist[:midpoint],item)
            else:
                return binarySearchRecursive(alist[midpoint+1:],item)

def sum(n):
    if (n == 1):
        return 1
    return sum(n-1) + n

print(sum(999))

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearchRecursive(testlist, 3))
print(binarySearchRecursive(testlist, 32))


