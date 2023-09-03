class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()  # Sort the array in ascending order
        closest_sum = float('inf')
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    return total
                
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total
                
                if total < target:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum

# Test cases
solution = Solution()
l=[-1,2,1,-4]
t=[0,0,0]

print(l)
print(t)
print(solution.threeSumClosest([-1,2,1,-4], 1)) # Output: 2
print(solution.threeSumClosest([0,0,0], 1))      # Output: 0
#Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
#Return the sum of the three integers.