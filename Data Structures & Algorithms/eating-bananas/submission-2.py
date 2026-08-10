class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # since piles[i] is non-zero, k cannot be zero ex. piles = [0] not possible, which would allow k=0 as a min.
        # no reason to eat more per hour than the max pile amount, else not minimum
        # therefore k in [1,highestK] must be true

        highestK = max(piles)
        # run a bin search from 1 -> highestK
        # for each i use as possible k value
            # if k > p[i] -> currH += 1
            # if k <= p[i] -> currH += rounded up p[i] / k
        # if cH > h break, we need more eating capacity -> l = mid + 1

        l, r = 1, highestK
        
        while l <= r:
            canK = (r + l) // 2

            currH = 0
            for p in piles:
                currH += math.ceil(p / canK)
                if currH > h:
                    break
            # if we took too long to eat, we need more eating capacity, this is not a valid k value since it produces a cH > h
            if currH > h:
                l = canK + 1
            # else see if we can push the k lower, at this point we know everything below this
            # gets us a cH value <= to h so we are in the clear
            else:
                # since we are in the clear we can check i these k's do better than our current
                r = canK - 1
        
        # algo is designed to zero in on the ONE number that gives us a minimum where our left pointer will always land
        return l