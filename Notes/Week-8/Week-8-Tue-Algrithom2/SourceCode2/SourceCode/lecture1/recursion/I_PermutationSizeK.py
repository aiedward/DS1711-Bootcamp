def perm(n, r):
    def perm(result, nums, r):
        if (r==0):
            print(result)
    
        for i in range(len(nums)):
            perm(result+str(nums[i]), nums[0:i]+nums[i+1:], r-1)
        
    nums = [str(_) for _ in range(1,n+1)]
    result = ''
    perm(result, nums, r)
    
perm(4,2)