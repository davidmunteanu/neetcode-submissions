class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        idx = 0;
        seen = set()

        for num in nums:
            if num in seen:
                seen.add(num)
            else:
                return True
    
        return False