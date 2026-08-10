class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        pre = [1] * len(nums)
        post = [1] * len(nums)

        n = len(nums)

        for i in range(n):
            if i == 0:
                continue
            pre[i] *= nums[i-1]
            pre[i] *= pre[i-1]
        
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                continue
            post[i] *= nums[i+1]
            post[i] *= post[i+1]
        
        for i in range(n):
            res[i] = pre[i] * post[i]
        return res

