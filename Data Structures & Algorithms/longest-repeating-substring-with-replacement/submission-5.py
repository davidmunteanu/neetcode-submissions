class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charFreq = defaultdict(int)
        maxFreq = 0
        left = 0
        length = 0

        for right in range(len(s)):
            charFreq[s[right]] += 1
            maxFreq = max(maxFreq, charFreq[s[right]])

            while (right - left + 1) - maxFreq > k:
                charFreq[s[left]] -= 1
                left += 1

            length = max(length, right - left + 1)
        
        return length