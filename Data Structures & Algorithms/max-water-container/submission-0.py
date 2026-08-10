class Solution:
    def maxArea(self, h: List[int]) -> int:
        i = 0
        j = len(h) - 1

        m = -1

        while i < j:
            l = h[i]
            r = h[j]

            area = min(l, r) * abs(i - j)
            if area > m:
                m = area
            
            if l < r:
                i += 1
            elif r < l:
                j -= 1
            else:
                i += 1
        
        return m

