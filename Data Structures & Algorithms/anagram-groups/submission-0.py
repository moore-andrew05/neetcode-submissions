from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = defaultdict(list)

        for s in strs:
            d = defaultdict(int)

            for c in s:
                d[c] += 1

            ret[tuple(sorted(d.items()))].append(s)

        return list(ret.values())