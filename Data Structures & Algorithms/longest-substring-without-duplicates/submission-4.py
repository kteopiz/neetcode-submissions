class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        res = 0

        # edge case of len <=1, just return length of s
        if len(s) <= 1:
            return len(s)
        
        l, r = 0, 0

        while r < len(s):
            if s[r] not in seen:
                seen[s[r]] = r
            else:
                res = max(res, r - l)
                lastSeen = seen[s[r]] + 1
                # ahead of window 
                if lastSeen >= l:
                    l = lastSeen
                seen[s[r]] = r
            r += 1
        return max(res, r - l)






