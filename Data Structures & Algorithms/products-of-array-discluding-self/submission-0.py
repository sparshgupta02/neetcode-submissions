class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        num_zeroes = nums.count(0)
        for num in nums:
            prod=prod*num
            
        res=[]
        if prod!=0:
            for num in nums:
                if num!=0:
                    res.append(prod//num)
        else:
            for i in range(len(nums)):
                if nums[i]!=0:
                    res.append(0)
                else:
                    prod=1
                    for j in range(len(nums)):
                        if(j!=i):
                            prod=prod*nums[j]
                    res.append(prod)
        return res

