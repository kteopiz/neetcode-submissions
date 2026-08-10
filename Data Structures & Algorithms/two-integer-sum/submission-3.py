class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {} # what is my pair to get target?

        # index : target - curr num
        # loop -> is my target in here? -> ht[target - curr num]
        # covers same numbers, since we map by index
        # [4,4] 0 and 1 will map cleanly if target == 8
        
        for i, n in enumerate(nums):
            if target - n in ht:
                return [ht[target-n], i]
            ht[n] = i   
            
        
        