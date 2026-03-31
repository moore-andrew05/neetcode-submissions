class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        OPERATORS = ['+', '-', '*', '/']   
        stk = []

        for tok in tokens:
            print(stk)
            if tok in OPERATORS: 
                num2 = int(stk.pop())
                num1 = int(stk.pop())

                if tok == '+':
                    stk.append(num1 + num2)
                elif tok == '-':
                    stk.append(num1 - num2)
                elif tok == '*':
                    stk.append(num1 * num2)
                elif tok == '/':
                    stk.append(int(num1 / num2))

            else:
                stk.append(tok)


        return int(stk[-1])
        