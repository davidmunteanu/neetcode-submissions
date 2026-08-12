class Solution:
    def isValid(self, s: str) -> bool:
        openStack = []
        match = {'{': '}', '(': ')', '[': ']'}

        for p in s:
            if p in [')', '}', ']']:
                if len(openStack) == 0 or match[openStack[-1]] != p:
                    return False
                
                openStack.pop()
            else:
                openStack.append(p)

        if len(openStack) != 0:
            return False
        
        return True
        