class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # len(nums) = n freq is the max something can appear
        # use a hash table to see the freq of each in 1 iteration
        # use fact 1, we can make "buckets" of frequency from 0 to n
        # go through the ht pairs and place them in their bucket
        # go reverse order from the top of the freq array to get the top k elements

        ht = {}

        for i in nums:
            if i in ht:
                ht[i] += 1
            else:
                ht[i] = 1

        # simple constant space, but worse case array size
        # buckets = [0] * len(nums)

        # trade off an iteration for space
        maxFreq = max(ht.values())

        # use list comp, to ensure each arr is own reference
        buckets = [[] for _ in range(maxFreq)]

        for key,v in ht.items():
            buckets[v - 1].append(key)
        
        res = []    
        i = maxFreq - 1

        while len(res) < k:
            if buckets[i]:
                res.append(buckets[i].pop(-1))
            else: 
                i -= 1
            print(res, buckets, len(res), i, len(res) < k)
        return res

