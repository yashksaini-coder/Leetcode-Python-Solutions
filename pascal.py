def generate_pascals_triangle_row(n):
    row = [1]  # Start with the first element as 1

    for i in range(1, n + 1):
        next_num = (row[i - 1] * (n - i + 1)) // i
        row.append(next_num)

    return row

# Take input from the user
n = int(input("Enter the level of Pascal's triangle: "))

# Generate the nth row of Pascal's triangle
pascal_row = generate_pascals_triangle_row(n)

# Print the result
print(pascal_row)
