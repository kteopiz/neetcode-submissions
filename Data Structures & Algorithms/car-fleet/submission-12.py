class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        ht = {}
        for i in range(len(position)):
            ht[position[i]] = speed[i]
        

        # v = d / t
        # vt = d
        # t = d / v

        # time of arrival == (target - position) / speed

        position.sort()

        time = []
        for i in range(len(position)):
            time.append((target - position[i]) / ht[position[i]])
        
        s = []

        for t in range(len(time)-1,-1,-1):
            if not s or time[t] <= s[0]:
                s.append(time[t])
            else:
                while s and time[t] > s[0]:
                    s.pop()
                res += 1
                s.append(time[t])
        # print(s)
        return res + 1 if len(s) else 0
