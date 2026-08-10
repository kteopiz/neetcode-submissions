class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        d = '*'
        for s in strs:
            # prefix delim character and a len(s)
            res += str(len(s)) + d + s
        return res

    def decode(self, s: str) -> List[str]:
        num = '' 
        res = []
        cs = ''
        
        i = 0

        while i < len(s):
            c = s[i]
            while c.isnumeric():
                num += c
                i += 1
                c = s[i]
            # skip delim, will always skip repeated delim in og string
            i += 1
            for j in range(int(num)):
                # pos i + j (involves len of wanted str)
                cs += s[i + j]
            res.append(cs)
            i += int(num)
            num = ''
            cs = ''
        return res