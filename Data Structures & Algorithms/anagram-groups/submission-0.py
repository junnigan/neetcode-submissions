class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for s in strs:
            comb=str(sorted(list(s)))
            if comb not in d:
                d[comb]=[s]
            else:
                d[comb].append(s)
        res=[x for _, x in d.items()]
        return res