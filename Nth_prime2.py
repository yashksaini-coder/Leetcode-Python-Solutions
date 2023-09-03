def prime_numbers(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for num in range(2, limit + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False
    return primes

def nth_prime(n, primes):
    return primes[n - 1]

if __name__ == '__main__':
    max_limit = 10 ** 6  # Adjust this limit based on your requirements
    primes = prime_numbers(max_limit)
    
    t = int(input("Enter test cases:-").strip())
    for _ in range(t):
        n = int(input("Enter a number:-").strip())
        result = nth_prime(n, primes)
        print(result)
