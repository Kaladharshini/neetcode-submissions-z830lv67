class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            k = tuple(count)
            res[k].append(s)
        
        finalRes = []
        for k, v in res.items():
            finalRes.append(v)
        
        return finalRes
        