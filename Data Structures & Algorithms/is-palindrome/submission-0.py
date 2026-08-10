class Solution:
    def isPalindrome(self, s: str) -> bool:

        # naively in terms of space
        res = ""
        for i in s:
            if i.isalnum():
                res += i
        
        l = 0
        r = len(res) - 1

        res = res.lower()

        while l < r:
            if res[l] != res[r]:
                return False
            l +=1
            r -= 1
        return True


        