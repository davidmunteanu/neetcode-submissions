class Solution:
    def isPalindrome(self, s: str) -> bool:
        startIdx = 0
        endIdx = len(s) - 1

        while startIdx < endIdx:
            while not s[startIdx].isalnum() and startIdx < endIdx:
                startIdx += 1
            while not s[endIdx].isalnum() and startIdx < endIdx:
                endIdx -= 1
            
            if s[startIdx].lower() != s[endIdx].lower():
                return False
            
            startIdx += 1; endIdx -= 1

        return True
        