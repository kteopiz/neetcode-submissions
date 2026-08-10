class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # there can be no more than len(nums) of any unique number
        ht = {}
        # implicitly sorted in increasing freq
        # since top of the list is the highest possible count
        track = [[] for n in nums]

        res = []

        # get freq of each n
        for n in nums:
            if n in ht:
                ht[n] += 1
            else:
                ht[n] = 1

        print(ht)

        for key in ht:
            freq = ht[key]
            track[freq - 1].append(key)
        
        print(track)

        i = len(nums) - 1
        while len(res) != k:
            freq_arr = track[i]
            if freq_arr:
                res.append(freq_arr.pop())
            else:
                i -= 1
            
        return res



       
                
                

