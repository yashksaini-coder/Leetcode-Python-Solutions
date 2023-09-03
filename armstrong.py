def is_armstrong_number(n):
    # Convert the number to a string to extract digits
    num_str = str(n)
    num_digits = len(num_str)
    
    # Calculate the sum of the cube of each digit
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum is equal to the original number
    return armstrong_sum == n

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    num = int(input())
    if is_armstrong_number(num):
        print("It is an ARMSTRONG number")
    else:
        print("It is NOT an ARMSTRONG number")
