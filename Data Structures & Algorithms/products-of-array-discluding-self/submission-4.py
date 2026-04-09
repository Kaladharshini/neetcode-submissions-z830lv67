class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = []
        prefix = 1
        res.append(prefix)
        for i in range(1, len(nums)):
            prefix *= nums[i-1]
            res.append(prefix)
        
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res