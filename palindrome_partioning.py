class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def is_palindrome(s):
            return s == s[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    path.append(s[start:end])
                    backtrack(end, path)
                    path.pop()

        result = []
        backtrack(0, [])
        return result

# Example usage:
s = "aab"
sol = Solution()
print(sol.partition(s))  # Output: [["a", "a", "b"], ["aa", "b"]]
