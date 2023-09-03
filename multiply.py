class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        a=int(num1)
        b=int(num2)
        c= str(a*b)
        return c
    

sol = Solution()

print("TEST CASE 1:-")
n1 = "2"
n2 = "3"
print("Num 1:-",n1)
print("Num 2:-",n2)
out=sol.multiply(n1,n2)
print("OUTPUT:-",out)


print("\nTEST CASE 2:-")
n1 = "123"
n2 = "456"
print("Num 1:-",n1)
print("Num 2:-",n2)
out=sol.multiply(n1,n2)
print("OUTPUT:-",out)