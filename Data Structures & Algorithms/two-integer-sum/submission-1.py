class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i,n in enumerate(nums):
            a[n]=i

        for i,n in enumerate(nums):
            diff = target-n
            if diff in a and a[diff]!=i:
                return [i,a[diff]]
        return []
        