class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = "".join(s.lower())
        new = "".join(char for char in new if char.isalnum())
        return new==new[::-1]


        