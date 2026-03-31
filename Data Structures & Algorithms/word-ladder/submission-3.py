class Cache:
    def __init__(self):
        self.cache = {}
        self.accesses = 0
        self.hits = 0

    def access(self, value):
        self.accesses += 1
        if value in self.cache:
            self.hits += 1
            return self.cache[value]
        else:
            return None

    def insert(self, key, value):
        self.cache[key] = value

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        cache = Cache()
        
        def recurse(curr_word, end_word, words_left):
            access = cache.access(curr_word)
            if access:
                return access

            if curr_word == end_word:
                return 1

            possible_words = []
            to_pop = []
            for i, word in enumerate(words_left):
                if sum([x != y for x, y in zip(curr_word, word)]) == 1:
                    possible_words.append((i, word))

            if not possible_words:
                return 10000
            
            print(curr_word)
            print(possible_words)
            # [words_left.pop(i) for i in to_pop]

            options = []
            for i, word in possible_words:
                copy = words_left[:]
                copy.pop(i)
                path = recurse(word, end_word, copy)
                cache.insert(word, path)
                options.append(path) 

            return 1 + min(options)

        ans = recurse(beginWord, endWord, wordList)
        if ans > 1000:
            return 0
        else: 
            return ans





            
        