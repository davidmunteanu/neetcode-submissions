class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        freq1 = defaultdict(int); freq2 = defaultdict(int)
        for c in s1: freq1[c] += 1
        for c in s2[:len(s1)]: freq2[c] += 1

        if freq1 == freq2: return True
        left, right = 0, len(s1)

        while right < len(s2):
            freq2[s2[left]] -= 1; left += 1
            freq2[s2[right]] += 1; right += 1
            if freq2[s2[left - 1]] == 0: del freq2[s2[left - 1]]

            if freq1 == freq2:
                return True

        return False 