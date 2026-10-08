class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        for i in range(len(position)):
            position[i] = (position[i], (target - position[i]) / speed[i])

        # sort by pos
        position.sort(key=lambda p: p[0])
        while position:
            curr = position.pop()

            # get rid of this fleet
            while position and position[-1][1] <= curr[1]:
                position.pop()
            
            res += 1
        
        return res





        




        

