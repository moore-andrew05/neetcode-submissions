class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        s_counts = defaultdict(int)
        t_counts = defaultdict(int)

        for i, char in enumerate(s):
            s_counts[char] += 1
            t_counts[t[i]] += 1

        return s_counts == t_counts


