class Solution:
    def encode(self, strs: List[str]) -> str:
        ret = ""
        for word in strs:
            length = len(word)
            separator = str(length)
            len_len = str(len(separator))
            ret += (len_len + separator + word)
        return ret

    def decode(self, s: str) -> List[str]:
        def gen(s):
            for char in s:
                yield char

        generator_string = gen(s)
        ret = []
    
        for char in generator_string:
            len_len = int(char)
            length = ""
            for _ in range(len_len):
                length += next(generator_string)

            length = int(length)

            word = ""

            for _ in range(length):
                word += next(generator_string)

            ret.append(word)


        return ret

                


