def largest_prime_factor(number):
    # Initialize the largest prime factor to 2
    largest = 2
    
    # Divide the number by 2 until it becomes odd
    while number % 2 == 0:
        number //= 2
    
    # Check for prime factors starting from 3
    factor = 3
    while factor * factor <= number:
        while number % factor == 0:
            largest = factor
            number //= factor
        factor += 2
    
    # If the remaining number is prime
    if number > 2:
        largest = number
    
    return largest

t = int(input("Enter test cases:-").strip())
for _ in range(t):
    n = int(input("Enter a number:-").strip())
    result = largest_prime_factor(n)
    print(result)
