class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        a = min(len(word1), len(word2))
        for i in range(a):
            result += word1[i]
            result += word2[i]
        if len(word1) > len(word2):
            result += word1[a:]
        if len(word1) < len(word2):
            result += word2[a:]
        return result