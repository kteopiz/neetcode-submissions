class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        for s in strs:
            c = [0] * 26
            for i in s:
                c[ord(i) - 97] += 1
            key = tuple(c)
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]
        
        return [g for g in groups.values()]
        