class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        ret = [0] * len(temperatures)
        
        for i, val in enumerate(temperatures):
            while stk and (val > stk[-1][1]):
                popidx, popval = stk.pop()
                ret[popidx] = i - popidx

            stk.append((i, val))
        return ret
            