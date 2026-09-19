class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVol = -sys.maxsize
        left = 0; right = len(heights) - 1

        while left < right:
            leftH = heights[left]
            rightH = heights[right]
            maxVol = max(maxVol, min(leftH, rightH) * (right - left))

            if leftH <= rightH:
                left += 1
            else:
                right -= 1

        return maxVol