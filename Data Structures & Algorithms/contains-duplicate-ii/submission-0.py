class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # k can be greater than the len(nums)
        
        #  if k >= len(nums), the question just becomes is there a duplicate in the array
        if k >= len(nums):
            return len(set(nums)) != len(nums)
        
        l = 0
        seen = set()

        # order of the question
            # invariant for the window: r-l <= k
            # condition for returning given the above holds
                # have i seen you before? 
                    # if yes return
                # if no
                    # if r-l < k -> add to set, push right pointer
                    # if r-l == k -> remove removed element at left, 
                        # we dont take the next element but we se

        for r in range(len(nums)):
            if r-l > k:
                seen.remove(nums[l])
                l += 1
            # correct the window should be ok
            if nums[r] in seen:
                return True
            seen.add(nums[r])
        return False