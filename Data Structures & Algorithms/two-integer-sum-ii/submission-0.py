class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            guess = numbers[left] + numbers[right]

            if guess == target:
                return [left + 1, right + 1]
            elif guess < target:
                left += 1
            elif guess > target:
                right -= 1