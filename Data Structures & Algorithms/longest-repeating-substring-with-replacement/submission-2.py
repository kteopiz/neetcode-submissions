class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # no jumping l pointer "beta"
        # highest freq element in the window is the one u want to switch to, the rest of the letters 
            # are arbitrary (?)

        # if len(window) - maxFreq <= k --> r +=1
            # this is because, we have enough operations of k to change everything to the maxFreq element
            # essentially means can we fit one more non maxFreq elem in, since we have an op to change it
        # else 
            # push left pointer up, we need to remove something from our window to fit the next one
        
        maxFreq = 1
        res = 0
        l = 0
        freq = {}
        # letter : freq in window

        for r in range(len(s)):

            freq[s[r]] = freq.get(s[r], 0) + 1
            maxFreq = max(freq[s[r]], maxFreq)

            while (r-l+1) - maxFreq > k:
                freq[s[l]] = freq.get(s[l], 0) - 1
                maxFreq = max(freq[s[l]], freq[s[r]], maxFreq)
                l += 1

            res = max(res, (r-l+1))
                
            
        return res


