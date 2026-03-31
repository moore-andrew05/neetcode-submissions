import torch
import torch.nn as nn
from torchtyping import TensorType

# torch.tensor(python_list) returns a Python list as a tensor
class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
        combo = positive + negative

        words = set()
        for chunk in combo:
            for word in chunk.split():
                words.add(word)

        sorted_words = sorted((list(words)))
        
        char_mapping = {}

        for idx, word in enumerate(sorted_words):
            char_mapping[word] = idx + 1

        def encode(sentence):
            integers = []
            for word in sentence.split():
                integers.append(char_mapping[word])
            return integers
        
        var_len_tens = []
        for sentence in combo:
            var_len_tens.append(torch.tensor(encode(sentence)))
        
        return nn.utils.rnn.pad_sequence(var_len_tens, batch_first=True)



    

