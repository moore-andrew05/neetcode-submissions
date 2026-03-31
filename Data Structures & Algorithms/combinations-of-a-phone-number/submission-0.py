class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_to_letters = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        res = []

        def backtrack(i, substr):
            if i >= len(digits):
                if len(substr) == len(digits) and len(substr) > 0:
                    res.append(substr)
                return

            possible = number_to_letters[digits[i]]

            for letter in possible:
                substr += letter
                backtrack(i + 1, substr)

                substr = substr[:-1]
                backtrack(i + 1, substr)

            
        backtrack(0, '')
        return res