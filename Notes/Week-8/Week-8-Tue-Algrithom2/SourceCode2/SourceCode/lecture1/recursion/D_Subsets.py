def subsets(nums):
    result = [[]]
    for num in nums:
        for element in result[:]:
            x=element[:]
            x.append(num)
            result.append(x)
    return result

def subsets_2(nums):
    res = [[]]
    for num in nums: 
        res += [ i + [num] for i in res]
    return res

def subsets_recursive(nums):
    list = []
    result = []
    subsets_recursive_helper(result, list, nums, 0);
    return result;

def subsets_recursive_helper(result, list, nums, pos):
    result.append(list[:])
    for i in range(pos, len(nums)):
        list.append(nums[i]) #
        subsets_recursive_helper(result, list, nums, i+1) #
        del list[-1] #
    
nums = [1, 2, 3]
print(subsets(nums))
print(subsets_2(nums))
print(subsets_recursive(nums))


