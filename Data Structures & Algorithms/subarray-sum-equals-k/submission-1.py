class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        res = 0
        seen = {0: 1}

        for num in nums:
            sum += num
            diff = sum - k

            res += seen.get(diff, 0)
            seen[sum] = seen.get(sum, 0) + 1
        
        return res