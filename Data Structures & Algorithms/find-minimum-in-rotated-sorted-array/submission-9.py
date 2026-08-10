class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float('inf')

        while l <= r:
            # Covers case of initially sorted array
           
            # but what else?
            if nums[l] <= nums[r]:
                return min(res, nums[l])
            
            m = (l + r) // 2

            # initial mid lands on min part of the pivot
            res = min(res, nums[m])
            
            # sort order holds to my left, pivot where min is cannot be there
            # cut out the sorted portion
            if nums[l] <= nums[m]:
                l = m + 1
            # unsorted to my left, cut right section to go towards it
            else:
                r = m - 1
        
        return res
                