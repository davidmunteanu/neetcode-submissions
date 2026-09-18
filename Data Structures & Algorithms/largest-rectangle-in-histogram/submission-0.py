class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for idx, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                h = heights[stack.pop()]
                w = idx - stack[-1] - 1 if stack else idx
                maxArea = max(maxArea, h * w)
                
            
            stack.append(idx)
        
        idx = len(heights)
        while stack:
                h = heights[stack.pop()]
                w = idx - stack[-1] - 1 if stack else idx
                maxArea = max(maxArea, h * w)

        return maxArea
