# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         groups = defaultdict(list)
#         for s in strs:
#             s_dict = defaultdict(int)
#             for char in s:
#                 s_dict[char] += 1
            
#             groups[frozenset(s_dict.items())].append(s)

       
#         return list(groups.values())
        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            res[tuple(sorted(s))].append(s)

        return list(res.values())