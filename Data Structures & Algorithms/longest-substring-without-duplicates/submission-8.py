class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ht = {}
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] not in ht:
                ht[s[r]] = r
            else:
                lastSeen = ht[s[r]]

                if lastSeen < l:
                    ht[s[r]] = r
                else:
                    l = lastSeen + 1
                    ht[s[r]] = r
            res = max(res, r - l + 1)
            
        return res


