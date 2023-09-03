class Solution(object):
    def firstMissingPositive(self,nums):
        n = len(nums)
        
        # First, move all positive integers to their correct positions.
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # Iterate through the modified array to find the missing positive integer.
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1
    
        

l=[1,2,0]
sol = Solution()
out = sol.firstMissingPositive(l)
print(out)
