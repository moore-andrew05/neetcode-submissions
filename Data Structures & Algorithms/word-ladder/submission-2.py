class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def recurse(curr_word, end_word, words_left):
            if curr_word == end_word:
                return 1
            possible_words = []

            to_pop = []
            for i, word in enumerate(words_left):
                if sum([x != y for x, y in zip(curr_word, word)]) == 1:
                    possible_words.append((i, word))
                    # to_pop.append(i)

            if not possible_words:
                return 10000
            
            print(curr_word)
            print(possible_words)
            # [words_left.pop(i) for i in to_pop]

            options = []
            for i, word in possible_words:
                copy = words_left[:]
                copy.pop(i)
                options.append(recurse(word, end_word, copy)) 

            return 1 + min(options)

        ans = recurse(beginWord, endWord, wordList)
        if ans > 1000:
            return 0
        else: 
            return ans





            
        