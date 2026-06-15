class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        words_map = defaultdict(list)
        for word in strs:
            vocab = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                vocab[index] += 1
            words_map[tuple(vocab)].append(word)
        return list(words_map.values())

                
