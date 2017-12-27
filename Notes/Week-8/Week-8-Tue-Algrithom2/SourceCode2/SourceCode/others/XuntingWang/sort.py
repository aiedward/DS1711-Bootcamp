#!/usr/bin/pythonf
from random import randint
import sys

class InvalidInputException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)


def merge_sort(array):
    """merge_sort: int array -> int array
        Purpose: Sort the input array of integers in descending order using the merge sort algorithm
        Example: merge_sort([4,5,1,3,2]) -> [5,4,3,2,1]
        Throws: InvalidInputException if list is None
    """
    # raise exception if list is none
    if array == None:
        raise InvalidInputException("invalid input")
    n = len(array)
    # if there is less or equal to 1 element in array
    if n < 1 or n == 1:
        return array
    # find the mid point
    mid = n//2
    # divide and conquer
    left = merge_sort(array[0:mid])
    right = merge_sort(array[mid:n])
    # merge the left and right
    array = merge(left,right)
    return array

def merge(A,B):
    """merge: int array * 2 -> int array
        Purpose: merge the two given array into one array in descending order
        Example: mege([7,2],[9,4,3]) -> [9,7,4,3,2]
    """
    # initialize merge
    result = []
    aInx = 0
    bInx = 0
    # enter while loop to compare numbers in A and B
    while aInx < len(A) and bInx < len(B):
        if A[aInx] > B[bInx] or A[aInx] == B[bInx]:
            result.append(A[aInx])
            aInx = aInx + 1
        else:
            result.append(B[bInx])
            bInx = bInx + 1
    # adding the remaining numbers in A or B
    # if terms remaining in A
    if aInx < len(A):
        result = result + A[aInx:len(A)]
    # if terms remaining in B
    if bInx < len(B):
        result = result + B[bInx:len(B)]
    return result

def quick_sort(array):
    """quick_sort: int array -> int array
        Purpose: Sort the input array of integers in descending order using the quicksort algorithm
        Example: quick_sort([4,5,1,3,2]) -> [5,4,3,2,1]
        Throws: InvalidInputException if list is None
    """
    # raise exception if list is none
    if array == None:
        raise InvalidInputException("invalid input")
    # base case
    if len(array) < 1 or len(array) == 1:
        return array
    # randomly find pivot
    pivotInx = randint(0,len(array)-1)
    pivot = array[pivotInx]
    # three lists holding numbers less, greater than or equal to pivot
    less = []
    equal = []
    greater = []
    # put elements into respective lists
    for element in array:
        if element < pivot:
            less.append(element)
        elif element > pivot:
            greater.append(element)
        else:
            equal.append(element)
    # concatenate three lists
    array = quick_sort(greater) + equal + quick_sort(less)
    return array

def radix_sort(array):
    """radix_sort: int array -> int array
        Purpose: Sort the input array of integers in descending order using the radixsort algorithm
        Example: radix_sort([4,5,1,3,2]) -> [5,4,3,2,1]
        Throws: InvalidInputException if list is None
    """
    # raise exception if list is none
    if array == None:
        raise InvalidInputException("invalid input")
    # instantiate buckets and an empty bucket, O(1)
    buckets = []
    length = len(array)
    for i in range(19):
        buckets.append([])
    # find the biggest number in this array, O(n)
    max_dig = len(str(find_absoluate_max(array)))
    # loop: from least to most significant place, O(d)
    for place in range(max_dig):
        # loop through every single element in number and sort, O(n)
        for number in array:
            # find the desired digit given the place
            string = str(abs(number))
            if len(string) < 1+ place:
                d = 0
            else:
                d = int(string[len(string)-1-place])
            # add number to buckets
            if number == 0 or number > 0:
                buckets[9-d].append(number)
            else:
                buckets[9+d].append(number)
        # concatenate array
        array = []
        for i in range(len(buckets)):
            array = array + buckets[i]
            if len(array) == length:
                break
        # empty buckets
        for i in range(19):
            buckets[i] = []
    return array

def find_absoluate_max(array):
    """find_max: int array -> array
        Purpose: find the maximum number in an array
        Example: find_max([8,9,17,2,5,89]) -> 89
    """
    max_number = -sys.maxsize
    for i in array:
#        if max_number < abs(i):
#            max_number = abs(i)
        max_number = max(max_number, i)
    return max_number

def main():
    array = [1,2,3,4,5]
    sorted_array = merge_sort(array)
    print(sorted_array)

    
if __name__ == "__main__":
    main()
