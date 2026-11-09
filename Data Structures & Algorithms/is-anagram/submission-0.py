class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict={}
        for ss in s:
            if ss in s_dict:
                s_dict[ss]+=1
            else:
                s_dict[ss]=0
        t_dict={}
        for tt in t:
            if tt in t_dict:
                t_dict[tt]+=1
            else:
                t_dict[tt]=0
        if s_dict==t_dict:
            return True
        else:
            return False