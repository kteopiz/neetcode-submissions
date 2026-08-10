class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        c = 0
        res = []

        # can remove the set if we do the while loop in else below
        # seen = set()

        while c < len(nums) - 1:
            if c != 0 and nums[c] == nums[c-1]:
                c += 1
                continue
            l = c + 1
            r = len(nums) - 1
            while l < r:
                curr = nums[c] + nums[l] + nums[r]
                if curr > 0:
                    r -= 1
                elif curr < 0:
                    l += 1
                else:
                    can = (nums[c], nums[l], nums[r])
                    res.append(can)
                    # get to next l candidate
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                    
                    # decrement of r will be handled by regular case
                    # since nums[l] is guranteed to NOT be the same , r will be guranteed invalid as well
                    # r -= 1
            c += 1
        return res
                    
