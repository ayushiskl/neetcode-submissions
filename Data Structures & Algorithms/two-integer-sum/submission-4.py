class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if -10000000 <= target <= 10000000 :

            if 2<= len(nums)<= 1000 :
                for i in range(len(nums)) :
                    if -10000000 <= nums[i] <= 10000000 :
                        for j in range(i+1 , len(nums)) :
                            if nums[i]+nums[j] == target :
                                return [i,j]