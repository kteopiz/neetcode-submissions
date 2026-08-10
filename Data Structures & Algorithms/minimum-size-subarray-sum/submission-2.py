class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        l = 0
        c = 0
        
        for r in range(len(nums)):
            c += nums[r]

            while c >= target:
                # print(l, r)
                res = min(res, r - l + 1)
                c -= nums[l]
                l += 1
            
        
        return 0 if res == float('inf') else res

