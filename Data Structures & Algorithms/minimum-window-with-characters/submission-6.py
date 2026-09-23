class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""

        mapt = defaultdict(int); maps = defaultdict(int)
        for c in t: mapt[c] += 1
        
        need, have = len(mapt), 0
        lens = sys.maxsize
        lefts, rights = -1, -1
        left = 0

        for right, c in enumerate(s):
            if c in mapt: 
                maps[c] += 1
                if maps[c] == mapt[c]: have += 1
                
            while have == need:
                if (right - left + 1) < lens: 
                    lefts, rights, lens = left, right + 1, right - left + 1

                if s[left] in mapt: 
                    maps[s[left]] -= 1
                    if maps[s[left]] < mapt[s[left]]: have -= 1
                left += 1
            
        if lefts == -1 or rights == -1:
            return ""
        else:
            return s[lefts:rights]