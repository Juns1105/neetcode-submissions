class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            k = (left + right) // 2
            elapsed_h =  sum( (p+k-1) // k for p in piles)

            if elapsed_h <= h:
                right = k
            else:
                left = k + 1
        return left

