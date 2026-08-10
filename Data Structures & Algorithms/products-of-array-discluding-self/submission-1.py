class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pre = [1] * len(nums)
        post = [1] * len(nums)

        for i in range(len(nums)):
            if i - 1 < 0:
                continue
            else:
                pre[i] = nums[i-1]
                pre[i] *= pre[i-1]

        for i in range(len(nums) - 1, -1, -1):
            if i + 1 > len(nums) - 1:
                continue
            else:
                post[i] = nums[i + 1]
                post[i] *= post[i + 1]
        
        res = [pre[i] * post[i] for i in range(len(nums))]

        return res