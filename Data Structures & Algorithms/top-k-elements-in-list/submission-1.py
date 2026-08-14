class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        if 1 <= len(nums) <= 10**4 :
            for i in nums:
                if -1000 <= i <= 1000:
                    if i not in dict1:
                        dict1[i] = 1
                    else:
                        dict1[i] +=1
            l = []
            new = dict(sorted(dict1.items() , key=lambda x: x[1], reverse=True))
            list1 = list(new.keys())
            for i in range(k):
                l.append(list1[i])
        return l