def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest_palindrome(limit):
    largest = 0
    for i in range(999, 99, -1):
        for j in range(999, i - 1, -1):
            product = i * j
            if product < limit and is_palindrome(product) and product > largest:
                largest = product
    return largest

if __name__ == '__main__':
    t = int(input("Enter test cases:-").strip())
    for _ in range(t):
        n = int(input("Enter a number:-").strip())
        result = largest_palindrome(n)
        print(result)
