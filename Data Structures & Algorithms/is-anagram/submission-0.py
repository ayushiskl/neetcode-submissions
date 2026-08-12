class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if 1 <= len(t) <= 5 * (10**4) and 1 <= len(s) <= 5 * (10**4) :
            s.lower()
            t.lower()
            if len(s) != len(t) :
                return False
            dict1 = {}
            dict2 = {}
            for i in range(len(s)) :
                if not s[i] in dict1:
                    dict1[s[i]] = 1
                else :
                    dict1[s[i]] += 1
            for i in range(len(t)) :
                if not t[i] in dict2:
                    dict2[t[i]] = 1
                else :
                    dict2[t[i]] += 1
            if dict1 == dict2 :
                return True
            else:
                return False