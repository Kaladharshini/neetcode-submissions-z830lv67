class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        result_count = [[] for i in range(len(nums) + 1)]
        for key, val in count.items():
            result_count[val].append(key)

        result = []
        for i in range(len(result_count)-1, 0, -1):
            for n in result_count[i]:
                result.append(n)
                if len(result) == k:
                    return result




        