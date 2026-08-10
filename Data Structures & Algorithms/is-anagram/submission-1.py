class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sort 
        # String equality comparison (n operations)

        # Hash table counter
        # space s + t -> n
        # time ^^

        return sorted(s) == sorted(t)