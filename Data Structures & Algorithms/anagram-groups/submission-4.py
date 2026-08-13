class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        if 1 <= len(strs) <= 10000 :
            for i in strs:
                if 0 <= len(i) <= 100 :
                    d = {}
                    for j in i.lower() :
                        if j not in d:
                            d[j] = 1
                        else :
                            d[j] += 1

                    key = tuple(sorted(d.items()))

                    if key not in anagrams:
                        anagrams[key] = []

                    anagrams[key].append(i)

        return list(anagrams.values())