class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = dict()
        for num, n in enumerate(nums):
            # nums = 0,1,2,3,4
            #n = value
            val = target - n
            if val in output:
                return [output[val],num]
            output[n] = num

            




        