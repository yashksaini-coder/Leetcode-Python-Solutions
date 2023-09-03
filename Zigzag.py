class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        current_row = 0
        direction = 1

        for char in s:
            rows[current_row] += char

            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1

            current_row += direction

        result = ''.join(rows)

        return result

# Example 1
s1 = "PAYPALISHIRING"
numRows1 = 3
solution = Solution()
output1 = solution.convert(s1, numRows1)
print(output1)  # Output should be "PAHNAPLSIIGYIR"

# Example 2
s2 = "PAYPALISHIRING"
numRows2 = 4
output2 = solution.convert(s2, numRows2)
print(output2)  # Output should be "PINALSIGYAHRPI"
