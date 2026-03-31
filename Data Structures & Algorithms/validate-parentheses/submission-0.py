class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        CTO = {')':'(',']':'[','}':'{'}
        stk = []
            
        for char in s:
            if char in CTO:
                if stk and stk[-1] == CTO[char]:
                    stk.pop()
                else:
                    return False

            else:
                stk.append(char)

        if stk:
            return False
        return True