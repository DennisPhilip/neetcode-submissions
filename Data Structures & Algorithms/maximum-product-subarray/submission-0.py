class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for n in nums:
            tmp = curMax * n
            curMax = max(n, curMax * n, curMin * n)
            curMin = min(n, tmp, curMin * n)
            res = max(res, curMax)
        return res