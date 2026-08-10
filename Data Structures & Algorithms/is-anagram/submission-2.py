class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sort 
        # String equality comparison (n operations)

        # Hash table counter
        # space s + t -> n
        # time ^^

        # n log n
        # return sorted(s) == sorted(t)

        sh = {}
        th = {}

        for i in s:
            if i in sh:
                sh[i] += 1
            else: 
                sh[i] = 1
                
        for i in t:
            if i in th:
                th[i] += 1
            else: 
                th[i] = 1

        return th == sh