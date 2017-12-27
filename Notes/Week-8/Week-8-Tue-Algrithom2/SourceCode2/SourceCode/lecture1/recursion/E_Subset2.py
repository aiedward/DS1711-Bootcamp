
def subsets2(nums):
    res = [[]]
    for num in nums: 
        res += [ i + [num] for i in res if i + [num] not in res]
    return res


def subsets_recursive2(nums):
    list = []
    result = []
    nums.sort()
    print(nums)
    subsets2_recursive_helper(result, list, nums, 0);
    return result;

def subsets2_recursive_helper(result, list, nums, pos):
    result.append(list[:])
    for i in range(pos, len(nums)):
        if (i != pos and nums[i] == nums[i-1]):
            continue;
        
        list.append(nums[i])
        subsets2_recursive_helper(result, list, nums, i+1)
        del list[-1]
    
nums = [1, 2, 3]
print(subsets2(nums))
print(subsets_recursive2(nums))

nums = [1,2,2]
print(subsets2(nums))
print(subsets_recursive2(nums))

