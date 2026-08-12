class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        neigh = set(nums)
        consMax = 0

        for num in neigh:
            cons = 0

            if num - 1 not in neigh:
                idx = num
                while idx in neigh:
                    idx += 1; cons += 1

                consMax = max(consMax, cons)

        return consMax
