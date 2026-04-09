class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashNum = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashNum:
                return [hashNum[diff], i]
            hashNum[nums[i]] = i
        