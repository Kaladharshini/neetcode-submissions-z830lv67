class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            k = tuple(count)
            freq[k].append(s)
        
        res = []
        for k, v in freq.items():
            res.append(v)

        return res