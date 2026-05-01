class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = sorted(s)
        print(a)
        b = sorted(t)
        print(b)
        return a == b