class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        s = set(nums)
        seen = set()
        for i in nums:
            streak = 1
            curr = i + 1
            while curr in s and curr not in seen:
                streak += 1
                curr += 1
            if streak > res:
                res = streak
        return res
            
            