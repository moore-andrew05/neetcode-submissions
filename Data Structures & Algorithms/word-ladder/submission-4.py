class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def gen_wildcards(word: str) -> list[str]:
            for i in range(len(word) - 1):
                yield word[:i] + "*" + word[i+1:]

            yield word[:-1] + "*"

        patterns = defaultdict(set)
        for word in wordList:
            for pattern in gen_wildcards(word):
                patterns[pattern].add(word)

        q = deque([(beginWord, 1)])
        visited = set()
        
        while q:
            word, depth = q.popleft()
            if word == endWord:
                return depth
            visited.add(word)

            for pattern in gen_wildcards(word):
                for word in patterns[pattern]:
                    if word not in visited:
                        q.append((word, depth + 1))

        return 0



            






