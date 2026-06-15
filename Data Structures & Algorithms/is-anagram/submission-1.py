class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        hash1 = Counter(s)
        hash2 = Counter(t)
        for key in hash1.keys():
            if hash1[key] != hash2[key]:
                return False
        for key in hash2.keys():
            if hash1[key] != hash2[key]:
                return False
        return True