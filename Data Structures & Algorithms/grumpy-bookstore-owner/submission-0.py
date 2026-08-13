class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        baseline = 0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                baseline += customers[i]
        
        window = 0
        maxGain = 0
        left = 0

        for right in range(len(customers)):
            if grumpy[right] == 1:
                window += customers[right]
            if right - left + 1 > minutes:
                if grumpy[left] == 1:
                    window -= customers[left]
                left += 1
            maxGain = max(maxGain, window)
        return baseline + maxGain