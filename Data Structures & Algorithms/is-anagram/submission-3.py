class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sort 
        # String equality comparison (n operations)

        # Hash table counter
        # space s + t -> n
        # time ^^

        # n log n
        # return sorted(s) == sorted(t)

        # prune obvious cases
        if len(s) != len(t):
            return False

        # n + m space and time
        # sh = {}
        # th = {}

        # for i in s:
        #     if i in sh:
        #         sh[i] += 1
        #     else: 
        #         sh[i] = 1
                
        # for i in t:
        #     if i in th:
        #         th[i] += 1
        #     else: 
        #         th[i] = 1

        # return th == sh

        # can do better space wise 
        sa = [0] * 26
        ta = [0] * 26

        LC_OFFSET = 97

        for i in s:
            sa[ord(i) - LC_OFFSET] += 1
        
        for i in t:
            ta[ord(i) - LC_OFFSET] += 1

        return ta == sa



