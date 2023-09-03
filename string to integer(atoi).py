class Solution(object):
    def myAtoi(self, s):
        s = s.lstrip()
        
        if not s:
            return 0
        
        sign = 1
        
        if s[0] in ('+', '-'):
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
        
        result = 0
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break
        
        result = sign * result
        result = max(min(result, 2**31 - 1), -2**31)
        
        return result

# Create an instance of the Solution class
solution = Solution()

# Pass the input string to the myAtoi method
input_str = "42"  # Replace this with your input string
output = solution.myAtoi(input_str)

# Print the result
print(output)
