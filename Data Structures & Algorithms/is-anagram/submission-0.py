class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        d_s = dict()
        d_t = dict()

        s_sort = "".join(sorted(s))
        t_sort = "".join(sorted(t))

        print(s_sort)
        print(t_sort)

        for i in s_sort:
            if i in d_s:
                d_s[i] +=1
            else:
                d_s[i] = 1

        for i in t_sort:
            if i in d_t:
                d_t[i] +=1
            else:
                d_t[i] =1
        print(d_s)
        print(d_t)

        return d_s == d_t





        