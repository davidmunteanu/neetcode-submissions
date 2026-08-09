class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        for word in strs:
            s += str(len(word)) + "#" + word

        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        idx = 0

        while idx < len(s) - 1:
            leng = s[idx : s.find("#", idx)]

            idx += len(leng) + 1
            strs.append(s[idx : idx + int(leng)])
            idx += int(leng)

        return strs
        
