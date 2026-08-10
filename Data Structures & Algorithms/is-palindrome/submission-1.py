class Solution:
    def isPalindrome(self, s: str) -> bool:

        # # naively in terms of space
        # res = ""
        # for i in s:
        #     if i.isalnum():
        #         res += i
        
        # l = 0
        # r = len(res) - 1

        # res = res.lower()

        # while l < r:
        #     if res[l] != res[r]:
        #         return False
        #     l +=1
        #     r -= 1
        # return True

        # do better by comparing in place
        l = 0
        r = len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
                # c a c 

    


        