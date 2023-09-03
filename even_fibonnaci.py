def even_fibonacci_sum(limit):
    a, b = 1, 2
    total_sum = 0
    while b <= limit:
        if b % 2 == 0:
            total_sum += b
        a, b = b, a + b
    return total_sum

if __name__ == '__main__':
    t = int(input("enter test cases:-").strip())
    for _ in range(t):
        n = int(input("enter a number:-").strip())
        result = even_fibonacci_sum(n)
        print(result)
