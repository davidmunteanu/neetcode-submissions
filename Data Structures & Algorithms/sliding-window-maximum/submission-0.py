class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque([(nums[0], 0)])

        for idx in range(1, k):
            while dq and dq[-1][0] < nums[idx]: dq.pop()
            dq.append((nums[idx], idx))
        
        result = [dq[0][0]]
        
        for right in range(k, len(nums)):
            while dq and dq[0][1] < right - k + 1: dq.popleft()
            while dq and dq[-1][0] < nums[right]: dq.pop()
            dq.append((nums[right], right))

            result.append(dq[0][0])

        return result