class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""

        mapt = defaultdict(int); maps = defaultdict(int)
        for c in t: mapt[c] += 1
        
        need, have = len(mapt), 0
        lens = sys.maxsize
        lefts, rights = -1, -1
        left, right = 0, 0

        while right < len(s):
            if s[right] in mapt: 
                maps[s[right]] += 1
                if maps[s[right]] == mapt[s[right]]: have += 1
                
            while have == need:
                if (right - left + 1) < lens: 
                    lefts, rights, lens = left, right + 1, right - left + 1

                if s[left] in mapt: 
                    maps[s[left]] -= 1
                    if maps[s[left]] < mapt[s[left]]: have -= 1
                left += 1
        
            right += 1
            
        if lefts == -1 or rights == -1:
            return ""
        else:
            return s[lefts:rights]