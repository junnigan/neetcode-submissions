class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            l=len(s)
            res+=str(l)+"#"+s
        return res
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        j=0
        while i<len(s) and j<len(s):
            if s[j]=="#":
                length=int(s[i:j])
                str_full=s[j+1:j+length+1]
                res.append(str_full)
                i=j+length+1
                j=i
            else:
                j+=1
        return res