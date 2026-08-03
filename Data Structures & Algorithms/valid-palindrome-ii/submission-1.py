class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrom(s: str) -> bool:
            for i in range(len(s) // 2):
                if s[i] != s[len(s) - i - 1]:
                    return False
            return True

        for i in range(len(s)):
            final_string = s[:i] + s[i+1:]
            if isPalindrom(final_string) == True:
                return True
        return False
        