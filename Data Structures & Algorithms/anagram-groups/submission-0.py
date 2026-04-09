from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)
        for s in strs:
            count = [0]*26
            for i in s:
                count[ord(i)-ord('a')]+=1
            result[tuple(count)].append(s)
        
        final_result = []
        for val in result.values():
            final_result.append(val)
        return final_result


        