class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        idx = 0;
        itemDict = {}

        while idx < len(nums):
            if itemDict.get(nums[idx], 0) == 0:
                itemDict[nums[idx]] = 1;
            else:
                return True

            idx += 1

        return False