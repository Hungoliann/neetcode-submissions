class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
        for i in range(len(nums)):
            y = target - nums[i]

            if y in dic and dic[y] != i:
                return [i, dic[y]]