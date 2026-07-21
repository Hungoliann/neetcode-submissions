class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for w in strs:
            key = ''.join(sorted(w))
            group.setdefault(key, []).append(w)
        return list(group.values())