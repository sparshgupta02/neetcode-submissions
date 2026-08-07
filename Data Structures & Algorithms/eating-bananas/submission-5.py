class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        res=0
        while(l<=r):
            m=(l+r)//2
            t = 0
            for pile in piles:
                t += math.ceil(pile / m)
            if(t<=h):
                res=m
                r=m-1
            elif(t>h):
                l=m+1
            
        return res