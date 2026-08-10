class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        check = [0] * 26
        state = [0] * 26
        matches = 0

        for i in range(len(s1)):
            check[ord(s1[i]) - ord('a')] += 1
            state[ord(s2[i]) - ord('a')] += 1

        for i in range(26):
            matches += 1 if check[i] == state[i] else 0
        
        if matches == 26:
            return True
        
        # Traverse window across
        l = 0

        # start at len(s1) since we have already traversed that many chars initializing the state
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            # take in new element
            idx = ord(s2[r]) - ord('a')
            state[idx] += 1
            if state[idx] == check[idx]:
                matches += 1
            elif check[idx] + 1 == state[idx]:
                matches -= 1
            
            idx = ord(s2[l]) - ord('a')
            state[idx] -= 1
            if state[idx] == check[idx]:
                matches += 1
            elif check[idx] - 1 == state[idx]:
                matches -= 1
            l += 1
        return matches == 26

            