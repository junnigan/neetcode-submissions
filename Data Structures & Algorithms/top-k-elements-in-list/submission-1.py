from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        count_list=[[] for _ in range(len(nums)+1)]
        for key, value in count.items():
            count_list[value].append(key)
        res=[]
        for i in range(len(count_list)-1,-1,-1):
            for num in count_list[i]:
                res.append(num)
                if len(res)==k:
                    return res