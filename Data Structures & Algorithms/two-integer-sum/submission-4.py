class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        for i in range(len(nums)):
            diff = target - nums[i] 
            if diff in ht:
                return [ht[diff], i]
            else:
                ht[nums[i]] = i
        return False
            # target = diff + i