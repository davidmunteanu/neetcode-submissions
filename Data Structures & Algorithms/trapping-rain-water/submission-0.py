class Solution:
    def trap(self, height: List[int]) -> int:
        rightMax = []
        volume = 0

        for idx in range(len(height) - 1, -1, -1):
            if not rightMax or height[rightMax[-1]] <= height[idx]:
                rightMax.append(idx)
        
        leftMax = 0
        for idx in range(len(height) - 1):
            if idx == 0 or not rightMax:
                continue
        
            if idx >= rightMax[-1]:
                rightMax.pop()

            volume += max(0, min(height[leftMax], height[rightMax[-1]]) - height[idx])

            if height[idx] > height[leftMax]:
                leftMax = idx

        return volume