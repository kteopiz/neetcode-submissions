class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = sorted(nums)

        res = []

        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                for k in range(j + 1, len(n)):
                    if -n[i] == n[j] + n[k] and [n[i], n[j], n[k]] not in res:
                            res.append([n[i], n[j], n[k]])
        return res