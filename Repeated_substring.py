class Solution(object):
    def repeatedSubstringPattern(self, s):
        n = len(s)
        
        for i in range(1, n):
            if n % i == 0 and s[:i] * (n // i) == s:
                return True
        
        return False

# Test cases
solution = Solution()
print(solution.repeatedSubstringPattern("abab"))         # Output: True
print(solution.repeatedSubstringPattern("aba"))          # Output: False
print(solution.repeatedSubstringPattern("abcabcabcabc")) # Output: True
