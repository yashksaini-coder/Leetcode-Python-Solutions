class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            area = h * w
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

import matplotlib.pyplot as plt
import numpy as np

n=np.arange(9)
height = [1,8,6,2,5,4,8,3,7]

plt.bar(n,height)
plt.show()
sol = Solution()
out = sol.maxArea(height)
print(out)