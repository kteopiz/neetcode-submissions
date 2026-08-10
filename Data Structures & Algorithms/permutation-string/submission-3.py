class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check = {}
        for s in s1:
            check[s] = check.get(s, 0) + 1

        l = 0

        while l < len(s2):
            curr = s2[l]

            if curr in check:
                can = s2[l:l+len(s1)]
                # print("c", can)

                temp = {}

                for c in can:
                    temp[c] = temp.get(c, 0) + 1
                # print("temp", temp)
                if temp == check:
                    return True
                else:
                    l += 1
                    while l < len(s2) and s2[l] not in temp:
                        l +=1
                        
            else:
                l+=1

        return False