class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0

        left, right = 0, 1
        subStr = 0

        windowChars = set()
        windowChars.add(s[left])

        while right < len(s):
            if s[right] in windowChars:
                subStr = max(subStr, right - left)
                windowChars.remove(s[left])
                left += 1
            else:
                windowChars.add(s[right])
                right += 1
        
        return max(subStr, right - left)