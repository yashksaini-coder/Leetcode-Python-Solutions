class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        x,y,z=nums[0],nums[1],nums[2]
        lis = [[x,y,z] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]

        return lis

sol = Solution()

nums = [1,2,3]
res=sol.permute(nums)

print(res)  