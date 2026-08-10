class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = {}
        res = []
        for s in strs:
            key = [0] * 26
            for c in s:
                # we can also count anagrams by freq of each letter
                key[ord(c) - ord('a')] += 1
            key = tuple(key)
            if key in ht:
                ht[key].append(s)
            else:
                ht[key] = [s]
        for v in ht.values():
            res.append(v)
        return res
        