def find_greatest_product(num, k):
    max_product = 0
    for i in range(len(num) - k + 1):
        product = 1
        for j in range(i, i + k):
            product *= int(num[j])
        max_product = max(max_product, product)
    return max_product

if __name__ == '__main__':
    t = int(input("Enter test cases:-").strip())
    for _ in range(t):
        n, k = map(int, input("Enter N & K respectively(10,5):-").strip().split())
        num = input("Enter a long number(e.g 3675356291):-").strip()
        result = find_greatest_product(num, k)
        print(result)
