class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if 0 <= len(nums) <= 10**5 :
            arr = []
            for i in range(len(nums)):
                if -10**9 <= nums[i] <= 10**9:
                    if nums[i] not in arr:
                        arr.append(nums[i])

        if arr == nums :
            return False
        else:
            return True