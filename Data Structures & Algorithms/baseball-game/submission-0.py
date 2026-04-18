class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []

        for _, val in enumerate(operations):
            if val=="+":
                i1=int(stk[-1])
                i2=int(stk[-2])
                stk.append(str(i1+i2))
                continue

            if val=="C":
                stk.pop()
                continue

            if val=="D":
                i1=int(stk[-1])
                stk.append(str(i1*2))
                continue

            stk.append(val)

        return sum([int(val) for val in stk])
            


        