class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # highest freq element in the window is the one u want to switch to, the rest of the letters 
        # this is because replacing all other letters for the most frequent one minimizes the replacements we need to do

        # if len(window) - maxFreq <= k --> r +=1
            # this is because, we have enough operations of k to change everything to the maxFreq element
            # essentially means can we fit one more non maxFreq elem in, since we have an op to change it
        # else 
            # push left pointer up, we need to remove something from our window to fit the next one
            # we push up UNTIL the window is valid, pushing once is not suffcient to find a valid window
            # again, this validaity can be solved by Len(window) - maxFreq <= k
        
        maxFreq = 1
        res = 0
        l = 0
        freq = {}
        # letter : freq in window

        for r in range(len(s)):

            # Track frequency first:
                # We cannot know if the window is valid without our frequencies updated

            freq[s[r]] = freq.get(s[r], 0) + 1
            maxFreq = max(freq[s[r]], maxFreq)
            
            # Must push until the window is valid, update frequencies (removal) as we go
            while (r-l+1) - maxFreq > k:
                freq[s[l]] = freq.get(s[l], 0) - 1
                maxFreq = max(freq[s[l]], freq[s[r]], maxFreq)
                l += 1

            # In a valid window with tracked frequencies we can update our res
            res = max(res, (r-l+1))
                
            
        return res


