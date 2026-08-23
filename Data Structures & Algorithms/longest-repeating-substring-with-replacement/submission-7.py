class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        maxFreq = 0 # guranteed one char in s
        res = 0
        l = r = 0
        while r < len(s):
            # start with a letter ALREADY IN
            # track counts FIRST, then check invariant
            # works initially because even as k = 0, any single letter is valid
            if s[r] in seen:
                seen[s[r]] += 1
            else:
                seen[s[r]] = 1
            maxFreq = max(maxFreq, seen[s[r]])

            # while window is invalid, keep removing from left window
            # cannot remove ONE else double count will occur at beginning of loop
            # can use a for loop because of this
            while k < (r - l + 1) - maxFreq:
                seen[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)
            r += 1
        return res
            



