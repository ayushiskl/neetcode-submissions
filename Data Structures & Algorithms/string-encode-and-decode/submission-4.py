class Solution:

    def encode(self, strs: List[str]) -> str:
        if 0 <= len(strs) < 100:
            l = ""
            for i in strs:
                if 0 <= len(i) < 200:
                    l += i+"||"
        return l

    def decode(self, s: str) -> List[str]:
        l = []
        l = s.split('||')
        return l[:-1]
