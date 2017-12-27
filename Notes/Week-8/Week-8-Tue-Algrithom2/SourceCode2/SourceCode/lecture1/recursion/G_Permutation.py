import math

def perm(result, nums):
    if (len(nums)==0):
        print(result)

    for i in range(len(nums)):
        perm(result+str(nums[i]), nums[0:i]+nums[i+1:])  #
    
nums = [2, 2, 3]
perm('', nums)
    
    
def permute(nums):
    perms = [[]]   
    for n in nums:
        new_perms = []
        for perm in perms:
            for i in range(len(perm)+1):   
                new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
        perms = new_perms
    return perms    

nums = [1, 2, 3]
print(permute(nums))


def getPermutation(n, k):
    nums = [str(_) for _ in range(1,n+1)]
    k -= 1
    ans = ""
    for i in range(n)[::-1]:
        ans += nums.pop(k // math.factorial(i))
        k %= math.factorial(i)
    return ans

nums = [1, 2, 3]
print(getPermutation(3,5))


