class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        for left_index in range(len(s)):
            string = set()
            for right_index in range(left_index, len(s)):
                if s[right_index] not in string:
                    string.add(s[right_index])
                else:
                    break
            result = max(result, len(string))

        return result
                



