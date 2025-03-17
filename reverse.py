# Method to reverse an array in-place
import numpy as np
class reverseArray:
    def __init__(self,arr):
        self.arr = arr
           
    def reverse_in_place(self):
        i=0
        j=len(self.arr)-1
        while i<j:
            temp=self.arr[i]
            self.arr[i]=self.arr[j]
            self.arr[j]=temp
            i+=1
            j-=1
        return self.arr

        
    # Method to reverse an array out-of-place
    # def reverse_out_of_place(self, arr):
    #     new_arr=np.zeros(len(arr),dtype=int)
    #     for i in range(len(arr)):
    #         new_arr[i]=arr[len(arr)-1-i]
    #     return  new_arr

# Tester code

array = [1, 2, 3, 4, 5]

# Testing in-place reversal
reverser = reverseArray(array)
print("Original array :", array)

# Testing in-place reversal
reverser.reverse_in_place()
print("In-place reversed array:", reverser.arr)

# Testing out-of-place reversal
reversed_array = reverser.reverse_out_of_place(array)
print("Out-of-place reversed array:", reversed_array)
