
def permUnique(result, nums):
    nums.sort()
    if (len(nums)==0):
        print(result)
    for i in range(len(nums)):
        if (i != 0 and nums[i] == nums[i-1]):
            continue;
        permUnique(result+str(nums[i]), nums[0:i]+nums[i+1:])
        
nums = [1, 2, 3]
permUnique('', nums)  
nums = [3, 2, 3]
permUnique('', nums)       


def permuteUnique(nums):
    ans = [[]]
    for n in nums:
        new_ans = []
        for l in ans:
            for i in range(len(l)+1):
                new_ans.append(l[:i]+[n]+l[i:])
                if i<len(l) and l[i]==n: break              #handles duplication
        ans = new_ans
    return ans


nums = [1, 2, 3]
print(permuteUnique(nums))

nums = [2, 2, 3]
print(permuteUnique(nums))