class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrom(s: str) -> bool:
            return s == s[::-1]

        for i in range(len(s)):
            final_string = s[:i] + s[i+1:]
            if isPalindrom(final_string) == True:
                return True
        return False
        