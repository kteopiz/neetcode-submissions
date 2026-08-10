class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0

        # use position as keys to their respective arrival times
        # v = d / t -> t = d / v
        times = {}
        for i in range(len(position)):
            p = position[i]
            position[i] = [p, (target-p) / speed[i]]
            # times[p] = (target - p) / speed[i]
        
        # sort by positions, go from the back, intuitively we process cars closest to the target first
        # also this position array will become our stack -> checking / popping from back will be easier
        position.sort(key=lambda p: p[0])

        while position:
            curr = position.pop()

            # while cars remain, and the current cars time is more than the ones before it pop off cars
            # this is because all the cars before it are going to catch up to the current car
            # seen by how the times before catch up to the current one
            while position and curr[1] >= position[-1][1]:
                position.pop()
            res += 1
        
        return res