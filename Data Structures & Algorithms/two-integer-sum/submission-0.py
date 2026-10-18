class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # {3 : 0}
        for i in range(len(nums)): # 
            if target - nums[i] in seen: # target-nums[0] = 4
                return [seen[target-nums[i]], i]
            seen[nums[i]] = i 
        