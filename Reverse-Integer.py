class Solution(object):
    def reverse(self, x):
        if x < 0:
            sign = -1
            x = abs(x)
        else:
            sign = 1

        reversed_x = 0
        while x != 0:
            print(x)
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x //= 10
            print(x)

        # Checking for overflow
        if reversed_x > 2**31 - 1 or reversed_x < -2**31:
            return 0

        return sign * reversed_x

sol = Solution()

out = sol.reverse(123)
print(out)  # Output should be 321
