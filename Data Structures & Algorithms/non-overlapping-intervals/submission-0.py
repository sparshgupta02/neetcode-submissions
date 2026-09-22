class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        cnt = 0
        lim = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]<lim:
                cnt+=1
            else:
                lim=intervals[i][1] 
        return cnt