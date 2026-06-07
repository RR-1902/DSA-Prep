from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        seen = defaultdict(int)
        seen[0] = 1
        for num in nums:
            prefix = prefix + num
            count += seen[prefix - k]
            seen[prefix] += 1
        return count
    
    #  TIME COMPLEXITY: O(n)
    #  SPACE COMPLEXITY: O(n)