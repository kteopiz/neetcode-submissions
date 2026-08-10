class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in nums:
            # if n = 3, if 3 - 1 = 2 not in set, its the middle of some sequence
            if n - 1 in num_set:
                continue
            else:
                curr = n
                running = 1

                while curr + 1 in num_set:
                    curr += 1
                    running += 1
                
                if running > longest:
                    longest = running
        
        return longest
