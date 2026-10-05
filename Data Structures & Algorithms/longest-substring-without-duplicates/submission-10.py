class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # char : index it was last seen at 
        lastSeen = {}
        l = 0
        res = 0
        # check if valid
        # update pointers to make it valid
        # try and update max
        # next iter

        for r in range(len(s)):
            if s[r] in lastSeen:
                l = max(l, lastSeen[s[r]] + 1)
            lastSeen[s[r]] = r
            res = max(res, r - l + 1)
        return res
            

        

        