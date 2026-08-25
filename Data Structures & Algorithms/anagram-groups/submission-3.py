class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)
        for word in strs:
            freq = [0 for i in range(26)]
            for char in word:
                freq[ord(char) - ord('a')] += 1
            res[tuple(freq)].append(word)
        final_res = []
        for v in res.values():
            final_res.append(v)
        return final_res