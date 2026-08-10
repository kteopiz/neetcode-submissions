class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # can sort -> go through each and see if next elem is ge then curr by 1
        # keep track of a max and curr streak of cons numbers for the return value
        # problem: O(nlogn) since we need to sort

        # save everything in ht
        # currElem
        # if currElem - 1 in 
            # 

        # O(n^2) using pattern from pre/post fix questiosn
        # m = 0
        # seen = set()
        # for i in nums:
        #     curr = 1
        #     pre = i - 1
        #     post = i + 1
        #     while pre in seen:
        #         curr += 1
        #         pre -= 1
        #     while post in seen:
        #         curr += 1
        #         post += 1
        #     if curr > m:
        #         m = curr
        #     seen.add(i)
        # return m

        # Do better, only start from a sequence BEGINNING
        m = 0
        s = set(nums)
        for i in nums:
            curr = 1
            if i-1 not in s:
                n = i + 1
                while n in s:
                    curr +=1 
                    n+=1
            if curr > m:
                m = curr
        return m



            

        