class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        for i in range(len(nums)):
            # if we have started w/ this num before, avoid it, will get dupe
            if i > 0 and nums[i] == nums[i-1]:
                continue
            curr = nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if curr + nums[l] + nums[r] > 0:
                    r -=1
                elif curr + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([curr, nums[l], nums[r]])

                    # do not want same starting value, shift it again
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res