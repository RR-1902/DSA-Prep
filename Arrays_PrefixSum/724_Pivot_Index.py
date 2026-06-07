class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        l = 0
        for i in range(len(nums)):
            right = total - nums[i] - l
            if l == right:
                return i
            l = l + nums[i]
        return -1
    
    #  TIME COMPLEXITY: O(n)
    #  SPACE COMPLEXITY: O(1)