class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        for i in range(len(nums)):
            past = 1 if i - 1 < 0 else nums[i-1]
            res[i] = res[i-1] * past 
        
        running = 1
        for i in range(len(nums) - 1, -1, -1):
            f = 1 if i + 1 > len(nums) - 1  else nums[i+1]
            running *= f
            res[i] *= running
        return res
        

        

            