class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # Initialize the pointer for the new length of the modified array
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Replace the element to be removed with the new element
                k += 1
        
        return k  # k represents the new length of the modified array

# Example usage
solution = Solution()
nums1 = [3, 2, 2, 3]
val1 = 3
length1 = solution.removeElement(nums1, val1)
print(length1)  # Output: 2, nums1 = [2, 2, ...]

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
length2 = solution.removeElement(nums2, val2)
print(length2)  # Output: 5, nums2 = [0, 1, 4, 0, 3, ...]
