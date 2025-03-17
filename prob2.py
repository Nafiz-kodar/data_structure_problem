# //// question 2 ////

import numpy as np

class sortArray:
    def __init__(self,arr):
        self.arr = arr
    
    def sort(self, a):
        length = len(a)
        no_of_positive_elements = 0
        output_arr = np.zeros(length,dtype=int)       #positive elements will be stored in this array first
        # print("Output array:", output_arr)
        pos_arr = np.zeros(no_of_positive_elements,dtype=int)          #positive elements will be stored in this array first
        neg_arr = np.zeros(length-no_of_positive_elements,dtype=int)   #negative elements will be stored in this array first

        for i in range(length):
            if a[i]>=0:
                no_of_positive_elements+=1
                pos_arr[i] = a[i]
        print("Output array1:", output_arr)

        for i in range(length):
            if a[i]<0:
                for j in range(len(output_arr)):
                    if output_arr[j] == 0:
                        output_arr[j] = a[i]
                        
        return output_arr
    

arr1 = [1, -1, 3, 2, -7, -5, 11, 6]
arr2 = [-5, 7, -3, -4, 9, 10, -1, 11]

sorter1 = sortArray(arr1)
sorted_arr1 = sorter1.sort(arr1)
print("Sorted array 1:", sorted_arr1)

sorter2 = sortArray(arr2)
sorted_arr2 = sorter2.sort(arr2)
print("Sorted array 2:", sorted_arr2)
        
