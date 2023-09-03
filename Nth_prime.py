def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def nth_prime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

if __name__ == '__main__':
    t = int(input("Enter test cases:-").strip())
    for _ in range(t):
        n = int(input("Enter a prime number:-").strip())
        result = nth_prime(n)
        print(result)
