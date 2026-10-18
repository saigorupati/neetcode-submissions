class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anas = defaultdict(list)
        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c)-ord('a')] += 1
            anas[str(arr)].append(s)
        
        return list(anas.values())