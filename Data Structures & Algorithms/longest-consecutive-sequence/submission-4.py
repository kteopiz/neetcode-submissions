class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # can sort -> go through each and see if next elem is ge then curr by 1
        # keep track of a max and curr streak of cons numbers for the return value
        # problem: O(nlogn) since we need to sort

        # save everything in ht
        # currElem
        # if currElem - 1 in 
            # 


        m = 0
        seen = set()
        for i in nums:
            curr = 1
            pre = i - 1
            post = i + 1
            while pre in seen:
                curr += 1
                pre -= 1
            while post in seen:
                curr += 1
                post += 1
            if curr > m:
                m = curr
            seen.add(i)
        return m

            

        