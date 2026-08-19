class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def feasible(maxSum):
            subarrays = 1
            currSum = 0

            for num in nums:
                if currSum + num > maxSum:
                    currSum = num
                    subarrays += 1
                else:
                    currSum += num
            return subarrays <= k

        l = max(nums)
        r = sum(nums)
        
        while l <= r:
            m = (l + r) // 2
            if feasible(m):
                r = m - 1
            else:
                l = m + 1
        return l