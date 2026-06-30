class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        output = False
        for i, val in enumerate(nums):
            if val in seen:
                output = True

            seen.add(val)
    
        return output