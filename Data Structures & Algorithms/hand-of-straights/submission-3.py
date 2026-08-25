class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:  
        if len(hand) % groupSize != 0:
            return False      
        count = Counter(hand)
        for num in sorted(count):
            if count[num] > 0:
                freq = count[num]

                for j in range(groupSize):
                    if count[num + j] < freq:
                        return False
                    count[num + j] -= freq

        return True

