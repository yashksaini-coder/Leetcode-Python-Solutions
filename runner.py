if __name__ == '__main__':
    # Take user input for the array
    n = int(input("Enter the number of elements in the array: "))
    arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

    # Initialize variables to keep track of the first and second maximum
    first_max = float('-inf')
    second_max = float('-inf')

    # Iterate through the array to find the first and second maximum elements
    for num in arr:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max and num != first_max:
            second_max = num

    # Print the second maximum element
    if second_max == float('-inf'):
        print("There is no second maximum element in the array.")
    else:
        print("The second maximum element is:", second_max)
