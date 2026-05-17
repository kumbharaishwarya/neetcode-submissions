class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_1 = "".join([char for char in s if char.isalnum()])
        return s_1==s_1[::-1]
        