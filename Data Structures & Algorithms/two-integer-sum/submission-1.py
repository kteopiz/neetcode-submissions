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
            # 7 - 3 = 4
            # 7 - 4 = 3
            diff[nums[i]] = i
        print(diff)
        for i in range(len(nums)):
            d = diff.get(target - nums[i], None)
            if d and i != d:
                return [i, diff[target-nums[i]]]
            