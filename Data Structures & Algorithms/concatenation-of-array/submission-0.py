class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [None] * 2 * l
        for idx, n in enumerate(nums):
            res[idx] = n
            res[idx + l] = n
        return res