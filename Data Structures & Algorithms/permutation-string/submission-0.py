class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map_s1 = [0] * 26
        for char in s1:
            map_s1[ord(char) - ord('a')] += 1

        if len(s1) > len(s2):
            return False

        map_s2 = [0] * 26
        for i in range(len(s1)):
            map_s2[ord(s2[i]) - ord('a')] += 1

            if map_s2 == map_s1:
                return True

        for j in range(len(s2) - len(s1)):
            map_s2[ord(s2[j]) - ord('a')] -= 1
            map_s2[ord(s2[j + len(s1)]) - ord('a')] += 1
            if map_s2 == map_s1:
                return True

        return False




        