class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}

        """
        4 -> 0
        3 -> 1
        2 -> 2
        1 -> 3
        """
        for i in range(len(nums)):
            d = target - nums[i]
            if d in diff: # what we need for nums[i] to hit target found alrd
                return [diff[d], i]
            else:
                diff[nums[i]] = i
            