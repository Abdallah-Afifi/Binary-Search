def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid  # Target found, return the index
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found in the array

def main():
    print("Welcome to the Binary Search Program!")

    # Example: Sorted list
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    target = int(input("Enter the number to search for: "))

    result = binary_search(sorted_list, target)

    if result != -1:
        print(f"{target} found at index {result}.")
    else:
        print(f"{target} not found in the list.")

if __name__ == "__main__":
    main()
