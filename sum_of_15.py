if __name__ == '__main__':
    t = int(input("enter test cases:-"))
    for _ in range(t):
        n = int(input("enter a number"))
        sum_3 = (3 * ((n - 1) // 3) * (((n - 1) // 3) + 1)) // 2
        sum_5 = (5 * ((n - 1) // 5) * (((n - 1) // 5) + 1)) // 2
        sum_15 = (15 * ((n - 1) // 15) * (((n - 1) // 15) + 1)) // 2
        result = sum_3 + sum_5 - sum_15
        print(result)
