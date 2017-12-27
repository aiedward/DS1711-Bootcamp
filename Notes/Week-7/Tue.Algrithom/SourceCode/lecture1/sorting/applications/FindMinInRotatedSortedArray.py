def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    j = len(nums) - 1
    while i < j:
        m = i + (j - i) // 2
        if nums[m] > nums[j]:
            i = m + 1
        else:
            j = m
    return nums[i]


def main():
    array1 = [4, 5, 6, 7, 0, 1, 2]
    result = findMin(array1)
    print (result)
    
    array2 = [4, 5, 6, 7, -2, -1, 0, 1, 2, 3]
    result = findMin(array2)
    print (result)
    
      
if __name__ == "__main__":
    main()