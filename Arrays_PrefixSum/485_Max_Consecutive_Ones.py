class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c1 = 0
        c2 = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                c1 = c1 + 1
                c2 = max(c1, c2)
            else:
                c1 = 0
        return c2
    
    #  TIME COMPLEXITY: O(n)
    #  SPACE COMPLEXITY: O(1)