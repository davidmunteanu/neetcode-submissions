class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resList = [1] * len(nums)

        left = 1
        right = 1

        for idx in range(len(nums)): 
            resList[idx] *= left
            resList[len(nums) - idx - 1] *= right

            left *= nums[idx]
            right *= nums[len(nums) - idx - 1]

        return resList