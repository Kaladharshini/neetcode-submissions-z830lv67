class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -1 * 1000000000000000000000
        for i in range(len(nums)):
            subArraySum = 0
            for j in range(i, len(nums)):
                subArraySum += nums[j]
                maxSum = max(maxSum, subArraySum)

        return maxSum