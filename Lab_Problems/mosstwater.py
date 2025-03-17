import numpy as np

def mostWater(arr):
    left_side = 0
    right_side = len(arr)-1
    max_area = 0
    height=0
    width = 0
    while left_side<right_side:
        width= right_side-left_side
        if arr[left_side]<arr[right_side]:
            height=arr[left_side]
            left_side+=1
        else:
            height=arr[right_side]
            right_side-=1
        if height*width>max_area:
            max_area=height*width
    print(max_area)



height = np.array([1,8,6,2,5,4,8,3,7])
print(f'Given Array: {height}')

print(f'\nExpected Output: 49')
print(f'Your Output: ',end='')
mostWater(height)