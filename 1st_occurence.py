class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0  # If needle is an empty string, return 0.

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i

        return -1  # If needle is not found in haystack, return -1.

# test case 1
haystack = "sadbutsad"
needle = "sad"

print("Haystack:-",haystack)
print("Needle:-",needle)
sol = Solution()
out = sol.strStr(haystack,needle)
print("OCCURENCE:-",out)

# Given two strings needle and haystack, return the index of the first occurrence
# of needle in haystack, or -1 if needle is not part of haystack.