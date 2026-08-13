class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for tempIdx, tempVal in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < tempVal:
                idx = stack.pop()
                result[idx] = tempIdx - idx
            stack.append(tempIdx)   

        return result