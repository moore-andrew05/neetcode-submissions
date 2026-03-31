from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for word in strs:
            code = [0] * 26
            for c in word:
                code[ord(c) - 97] += 1

            d[tuple(code)].append(word)


        return list(d.values())