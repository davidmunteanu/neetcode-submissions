class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, 0
        candidateK = sys.maxsize
        for pile in piles:
            right = max(right, pile)

        while left <= right:
            mid = int((left + right) / 2)

            trialH = 0
            for pile in piles:
                trialH += math.ceil(pile / mid)

            if trialH > h:
                left = mid + 1
            else:
                candidateK = min(candidateK, mid)
                right = mid - 1
        
        return candidateK