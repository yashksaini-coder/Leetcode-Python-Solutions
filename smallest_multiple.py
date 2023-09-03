def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def smallest_multiple(limit):
    result = 1
    for i in range(1, limit + 1):
        result = lcm(result, i)
    return result

if __name__ == '__main__':
    t = int(input("Enter test cases:-").strip())
    for _ in range(t):
        n = int(input("Enter a number:-").strip())
        result = smallest_multiple(n)
        print(result)
