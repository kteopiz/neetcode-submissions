class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            group = [0] * 26
            for c in s:
                group[97 - ord(c)] += 1
            if tuple(group) in groups:
                groups[tuple(group)].append(s)
            else:
                groups[tuple(group)] = [s]

        return list(groups.values())


            