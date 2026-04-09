class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashNum = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashNum:
                return [hashNum[diff], i]
            hashNum[nums[i]] = i

        """for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
"""
        