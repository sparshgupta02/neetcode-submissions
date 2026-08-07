class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n,m=len(nums1),len(nums2)
        i=j=0
        med1=med2=0
        for count in range((n+m)//2+1):
            med2=med1
            if i<n and j<m:
                if nums1[i]>nums2[j]:
                    med1=nums2[j]
                    j+=1
                else:
                    med1 =nums1[i]
                    i+=1
            elif i<n:
                med1=nums1[i]
                i+=1
            else:
                med1=nums2[j]
                j+=1
        if(n+m)%2==1:
            return float(med1)
        else:
            return (med1+med2)/2.0
