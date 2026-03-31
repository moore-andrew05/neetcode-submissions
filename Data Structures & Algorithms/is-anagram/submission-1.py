from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s = defaultdict(int)
        d_t = defaultdict(int)

        for c in s:
            d_s[c] += 1

        for c in t:
            d_t[c] += 1

        return d_s == d_t