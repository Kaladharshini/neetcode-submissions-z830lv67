class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        freq = defaultdict(list)
        for key, val in count.items():
            freq[val].append(key)

        res = []

        for c in range(len(nums), 0, -1):
            if c in freq:
                for n in freq[c]:
                    res.append(n)
                    if len(res) == k:
                        return res

