class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

       numset= set(numbers)
       for i in range(len(numbers)):
        if (target-numbers[i]) in numset:
            k=target-numbers[i]
            indices = [r for r, val in enumerate(numbers) if val == k]
            for j in indices:
                if i!=j:
                    return [i+1,j+1]



