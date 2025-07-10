import random

# Generate a list of 5 random integers between 0 and 9
numbers = [random.randrange(0, 10) for _ in range(5)]
# Randomly choose a window size of 1 or 2
window_size = random.randrange(1, 3)
# Initialize the maximum sum as the sum of the first window
max_sum = sum(numbers[:window_size])
# Initialize the current window total
current_sum = max_sum
# start_index is the start index of the window
start_index = 0
# max_start and max_end will store the indices of the window with the maximum sum
max_start = 0
max_end = window_size - 1
# Slide the window through the list
for end_index in range(window_size, len(numbers)):
    current_sum = current_sum + numbers[end_index]  # Add the next element to the window
    current_sum = current_sum - numbers[start_index]  # Remove the element that is no longer in the window
    if current_sum > max_sum:
        max_sum = current_sum  # Update max sum if current window is greater
        max_start = start_index + 1     # Update start index of max window
        max_end = end_index         # Update end index of max window
    start_index += 1  # Move the window forward
# Print the random list and window size
print(numbers, window_size)
# Print the maximum sum and the indices of the window
print(max_sum, max_start, max_end)
