class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        c = 0
        res = []
        seen = set()

        while c < len(nums) - 1:
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
                    if can not in seen:
                        res.append(can)
                        seen.add(can)
                    l += 1
                    r -= 1
            c += 1
        return res
                    
