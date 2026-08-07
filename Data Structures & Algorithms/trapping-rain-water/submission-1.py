class Solution:
    def trap(self, height: List[int]) -> int:
        curr_max=height[0]
        l=len(height)
        pref_max,suff_max=[],[]
        res=0
        for i in range(len(height)):
            if height[i]>curr_max:
                curr_max=height[i]
            pref_max.append(curr_max)
        curr_max=height[l-1]
        for i in range(len(height)-1,-1,-1):
            if height[i]>curr_max:
                curr_max=height[i]
            suff_max.append(curr_max)
        suff_max=suff_max[::-1]
        for i in range(1,l-1):
            res+=max(min(pref_max[i], suff_max[i]) - height[i],0)
        return res