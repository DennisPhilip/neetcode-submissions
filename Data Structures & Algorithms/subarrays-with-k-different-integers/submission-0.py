class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(nums, k):
            count = {}
            l = res = 0

            for r in range(len(nums)):
                count[nums[r]] = count.get(nums[r], 0) + 1

                while len(count) > k:
                    count[nums[l]] -= 1

                    if count[nums[l]] == 0:
                        del count[nums[l]]
                    
                    l += 1
                res += r - l + 1
            
            return res

        return atMostK(nums, k) - atMostK(nums, k - 1)