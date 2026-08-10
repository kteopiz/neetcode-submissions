class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_ht = {}
        t_ht = {}
        for c in s:
            if c in s_ht:
                s_ht[c] += 1
            else:
                s_ht[c] = 1
        for c in t:
            if c in t_ht:
                t_ht[c] += 1
            else:
                t_ht[c] = 1
        return s_ht == t_ht