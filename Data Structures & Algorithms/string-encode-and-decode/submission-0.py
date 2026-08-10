class Solution:
    delim = '/'

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += s
            res += self.delim
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        running = ''

        for c in s:
            if c == self.delim:
                res.append(running)
                running = ''
                continue
            else:
                running += c
        return res
