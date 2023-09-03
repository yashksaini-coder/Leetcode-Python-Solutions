class Solution(object):
    def isPalindrome(self, x):
        # Convert the integer to a string
        x_str = str(x)
        
        # Check if the string is equal to its reverse
        return x_str == x_str[::-1]



sol = Solution()
num=121
out = sol.isPalindrome(num)

print(out)