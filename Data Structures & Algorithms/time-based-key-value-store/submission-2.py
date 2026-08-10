class TimeMap:

    def __init__(self):
        # key : [(timestamp, value)]
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # can always append without worry of breaking order since ts also strictly increasing
        if key in self.store:
            self.store[key].append([timestamp, value]) 
        else:
            self.store[key] = [[timestamp, value]]
    def get(self, key: str, timestamp: int) -> str:
        # ts, val
        res = (-1, "")

        # invalid key that has not been set
        if key not in self.store:
            return res[1]
        
        # space in which we are searching
        search = self.store[key]

        l,r = 0, len(search) - 1

        while l <= r:
            m = (r + l) // 2
            tsp, val = search[m]
            
            # hit the exact val
            if tsp == timestamp:
                res = (tsp, val)
                break

            # if tsp < ts holds
            # and greater than our current best which is max # below ts, update
            # we only update res if the tsp is greater than the one we have already seen
            # this is because while tsp < ts makes this a candidate, if it is not the max tsp seen we dont want it
            if tsp < timestamp:
                if tsp > res[0]:
                    res = (tsp, val)
                l = m + 1 
            else:
                r = m - 1
        return res[1]

        
