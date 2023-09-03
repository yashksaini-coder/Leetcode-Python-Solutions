class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = zip(*matrix[::-1])

sol=Solution()

#test case 1
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("Matrix:-\n")
print("[[1,2,3]","\n","[4,5,6]","\n","[7,8,9]]")

# code is modified to fit into python3 version
