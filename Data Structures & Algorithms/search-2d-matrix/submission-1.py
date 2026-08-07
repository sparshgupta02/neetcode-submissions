class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m=len(matrix)
        n=len(matrix[0])
        l,r=0,m*n-1
        while l<=r:
            k=l+(r-l)//2
            a=k//n
            b=k%n
            if matrix[a][b] == target:
                return True
            elif matrix[a][b] < target:
                l = k + 1
            else:
                r = k - 1
        return True if(matrix[a][b]==target) else False