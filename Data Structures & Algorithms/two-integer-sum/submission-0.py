class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in output:
                return [output[val], i]
            else:
                output[nums[i]] = i