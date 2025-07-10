# Merge Sort implementation in Python

def split_it(data_list):
    # If the list has more than one element, split it
    if len(data_list) > 1:
        mid = len(data_list) // 2  # Find the middle index
        left_split = data_list[: mid]  # Left half
        right_split = data_list[mid:]  # Right half
        # Recursively split both halves
        split_it(left_split)
        split_it(right_split)
        # Merge the sorted halves
        merge_sorted(left_split, right_split, data_list)


def merge_sorted(left_split, right_split, data_list):
    la = len(left_split)
    lb = len(right_split)
    i = j = k = 0  # Initialize pointers for left, right, and merged list

    # Merge elements from left and right into data_list
    while i < la and j < lb:
        if left_split[i] < right_split[j]:
            data_list[k] = left_split[i]
            i += 1
        else:
            data_list[k] = right_split[j]
            j += 1
        k += 1
    # Copy any remaining elements from left_split
    if i < la:
        data_list[k:] = left_split[i:]
    # Copy any remaining elements from right_split
    if j < lb:
        data_list[k:] = right_split[j:]

# Main function to test merge sort
def main():
    li = [22, -1, 0, 3999999, 12, 4545, 2578, 5, 6, 4]  # Sample list
    split_it(li)  # Sort the list
    print(li)  # Print the sorted list


main()  # Run the main function
