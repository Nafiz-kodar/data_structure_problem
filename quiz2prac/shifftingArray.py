def right_shift_array(arr):
    if len(arr) == 0:
        return arr
    last_element = arr[-1]
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = last_element
    return arr

def left_shift_array(arr):
    if len(arr) == 0:
        return arr
    first_element = arr[0]
    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]
    arr[-1] = first_element
    return arr


# Example usage
array = [1, 2, 3, 4, 5]
rshifted_array = right_shift_array(array)
lshifted_array = right_shift_array(array)
print(rshifted_array)  # Output: [5, 1, 2, 3, 4]
print(lshifted_array)  # Output: [5, 1, 2, 3, 4]

