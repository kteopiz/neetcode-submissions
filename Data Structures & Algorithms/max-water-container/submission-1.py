class Solution:
    def maxArea(self, h: List[int]) -> int:
        l = 0
        r = len(h) - 1
        m = 0
        while l < r:
            curr = min(h[l], h[r]) * (r - l)
            m = max(m, curr)

            if h[l] < h[r]:
                l += 1
            elif h[l] > h[r]:
                r -=1
            else:
                l += 1
        return m