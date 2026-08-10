class Solution:
    def characterReplacement(self,  s: str, k: int) -> int:
        res = 0 

        # continue, when a problem occurs deal with it and the res

        ht = {}
        maxFreq = 0
        l = 0 

        for r in range(len(s)):
            # we add in the current element, therefore window validity is in question
            ht[s[r]] = ht.get(s[r], 0) + 1
            maxFreq = ht[s[r]] if ht[s[r]] > maxFreq else maxFreq

            # windowSize - maxFreq <= k means window is valid

            # ensure validity of the window before recording a result
            # cannot record an invalid result
            while (r-l+1) - maxFreq > k:
                ht[s[l]] = ht.get(s[l], 0) - 1
                l += 1 
            
            res = max(res, (r-l+1))
        return res
