class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []

        for right, x in enumerate(nums):
            if dq and dq[0][1] <= right - k:
                dq.popleft()
            
            while dq and dq[-1][0] < x:
                dq.pop()

            dq.append((x, right))

            if right >= k - 1:
                result.append(dq[0][0])

        return result