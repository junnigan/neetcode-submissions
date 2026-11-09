class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for s in strs:
            comb=tuple(sorted(s))
            if comb not in d:
                d[comb]=[s]
            else:
                d[comb].append(s)
        return list(d.values())