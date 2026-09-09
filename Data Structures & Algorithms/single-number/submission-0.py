class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s=set()
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                s.remove(num)
        k= list(s)[0]
        return k