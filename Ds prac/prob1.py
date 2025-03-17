####  ARRAY

# //// question 1 ////

import numpy as np

a = np.zeros(int(input("Enter the size of the array: ")))
b = np.zeros(int(input("Enter the size of the array: ")))

for i in range(len(a)):
    a[i] = int(input(f"Enter element {i+1}: "))


for i in range(len(b)):
    b[i] = int(input(f"Enter element {i+1}: "))

print(f"Array after insertion: {a}")
print(f"Array after insertion: {b}")

class Union:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def union(self):
        count=len(a)+len(b)
        for i in range(len(a)):
            for j in range(len(b)):
                if a[i] == b[j]:
                    count -= 1
                
        return count
    

u = Union(a, b)
print(u.union())


