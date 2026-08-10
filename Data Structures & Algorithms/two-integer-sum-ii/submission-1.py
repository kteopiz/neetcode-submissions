class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        l = 0
        r = len(n) - 1

        while l < r:
            curr = n[l] + n[r]
            if curr < target:
                l +=1
            elif curr > target:
                r -= 1
            else:
                return [l + 1, r + 1]

    