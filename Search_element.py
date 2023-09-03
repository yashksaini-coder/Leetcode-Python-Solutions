class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1

solution = Solution()
nums1 = [4, 5, 6, 7, 0, 1, 2]
target1 = 0
print(solution.search(nums1, target1))  # Output: 4

nums2 = [4, 5, 6, 7, 0, 1, 2]
target2 = 3
print(solution.search(nums2, target2))  # Output: -1

nums3 = [1]
target3 = 0
print(solution.search(nums3, target3))  # Output: -1
