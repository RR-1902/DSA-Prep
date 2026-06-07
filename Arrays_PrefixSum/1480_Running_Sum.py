class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        c = 0
        for i in nums:
            c = c + i
            result.append(c)
        return result
    

    #  TIME COMPLEXITY: O(n)
    #  SPACE COMPLEXITY: O(n)