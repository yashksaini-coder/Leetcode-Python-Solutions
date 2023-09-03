class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = ""
        while columnNumber > 0:
            # Convert to 0-based index
            columnNumber -= 1
            remainder = columnNumber % 26
            result = chr(65 + remainder) + result
            columnNumber //= 26
        return result

# Example usage
sol = Solution()
n=int(input("Enter a number:-"))
out = sol.convertToTitle(n)
print(out)
