from util.ArrayUtil import ArrayUtil
from random import randint
import sys

def findMissing(list):
    length = len(list)
    sum = 0
    for i in range(length+1):
        sum += i

    for i in range(length):
        sum -= list[i]
        
    return sum

def findMissing2(list):
    buckets = [0] * 10
    
    for i in range(9):
        buckets[list[i]] = 1
    result = -1
    for i in range(10):
        if buckets[i] != 1:
            result = i
            break
    return result
    
def findMissing3(list):
    length = len(list)
    sum = 0
    for i in range(length+1):
        sum ^= i

    for i in range(length):
        sum ^= list[i]
        
    return sum
    
def main():
    util = ArrayUtil()
    list = util.generateRandomArray(10)
    util.printList(list)
    r = randint(0,9)
    print(r, ": ", list[r])
    list.pop(r)
    util.printList(list)
    missing = findMissing(list)
    print("missing1: ", missing)
    missing = findMissing2(list)
    print("missing2: ", missing)
    missing = findMissing3(list)
    print("missing3: ", missing)
    
main()

print(sys.maxsize)
print(sys.maxsize * sys.maxsize)




    
