class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for num in nums:
            if num not in d:
                d[num]=1
            else:
                d[num]+=1
        d=dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        res=[]
        i=0
        for key in d.keys():
            if i<k:
                res.append(key)
                i+=1
            else:
                break
        return res