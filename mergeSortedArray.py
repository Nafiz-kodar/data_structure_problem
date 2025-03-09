import numpy as np
import unittest

# Given two sorted arrays, merge them into one sorted array

def mergeSortedArray(arr1, arr2):
    new_arr=np.empty(len(arr1)+len(arr2), dtype=int)
    i=0
    j=0
    new=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            new_arr[new]=arr1[i]
            i+=1
            new+=1
        else:
            new_arr[new]=arr2[j]
            j+=1
            new+=1
    while i<len(arr1):
        new_arr[new]=arr1[i]
        i+=1
        new+=1
    while j<len(arr2):
        new_arr[new]=arr2[j]
        j+=1
        new+=1
    return new_arr


a1 = np.array([1, 2, 3])
print(f'Sorted Array 1: {a1}')
a2 = np.array([2, 5, 6])
print(f'Sorted Array 2: {a2}')
returned_value = mergeSortedArray(a1, a2)
print(f'Merged Sorted Array: {returned_value}\n') # This should print [1, 2, 2, 3, 5, 6]
unittest.output_test(returned_value, np.array([1, 2, 2, 3, 5, 6]))

print('\n==================================\n')

a3 = np.array([1, 3, 5, 11])
print(f'Sorted Array 3: {a3}')
a4 = np.array([2, 7, 8])
print(f'Sorted Array 4: {a4}')
returned_value = mergeSortedArray(a3, a4)
print(f'Merged Sorted Array: {returned_value}\n') # This should print [1, 2, 3, 5, 7, 8, 11]
unittest.output_test(returned_value, np.array([1, 2, 3, 5, 7, 8, 11]))