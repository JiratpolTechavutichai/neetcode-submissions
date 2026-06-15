class Solution:
    def isPalindrome(self, s: str) -> bool:
        concate = ''.join(char.lower() for char in s if char.isalnum())
        for i in range(len(concate) // 2):
            if concate[i] != concate[len(concate) - 1 - i]:
                return False
        return True



        