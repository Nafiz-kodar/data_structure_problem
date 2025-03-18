"""////Question 1////"""
import numpy as np

# def compress_matrix(mat):
#     """
#     Compress a 2D matrix by grouping elements in 2x2 blocks and summing them
    
#     Args:
#         mat: 2D array with even number of rows and columns
        
#     Returns:
#         Compressed 2D array
#     """
#     rows, cols = len(mat), len(mat[0])
#     compressed_rows, compressed_cols = rows // 2, cols // 2
    
#     # Initialize the compressed matrix
#     compressed = np.zeros((compressed_rows,compressed_cols), dtype=int)
    
#     # Process each 2x2 block
#     for i in range(0, rows, 2):
#         for j in range(0, cols, 2):
#             # Sum the 2x2 block
#             block_sum = mat[i][j] + mat[i][j+1] + mat[i+1][j] + mat[i+1][j+1]
#             compressed[i//2][j//2] = block_sum
    
#     return compressed

# # Test the function with the given example
# if __name__ == "__main__":
#     # Create the sample input matrix
#     mat = np.array([
#         [1, 2, 3, 4],
#         [5, 6, 7, 8],
#         [1, 3, 5, 2],
#         [-2, 0, 6, -3]
#     ])
    
#     print("Input Matrix:")
#     print(mat)
    
#     result = compress_matrix(mat)
#     print("\nCompressed Matrix:")
#     print(result)

"""////Question 2////"""
# def print_matrix(m):
#   row,col = m.shape
#   for i in range(row):
#     c = 1
#     print('|', end='')
#     for j in range(col):
#       c += 1
#       if(len(str(m[i][j])) == 1):
#         print(' ',m[i][j], end = '  |')
#         c += 6
#       else:
#         print(' ',m[i][j], end = ' |')
#         c += 6
#     print()
#     print('-'*(c-col))

# def sum_diff(matrix):
#     row=len(matrix)
#     col=len(matrix[0])
#     arr=np.zeros((row,col), dtype=int)
#     for j in range(col):
#       sum=0
#       for i in range(row):
#         sum+=matrix[i][j]
#         arr[i][j]=sum

#     arr2=np.zeros((1,col-1),dtype=int)
#     for i in range(col-1):
#         n=arr[row-1][i+1]-arr[row-1][i]
#         arr2[0][i]=n
#     return arr2

# matrix=np.array([[1,3,1],
#                  [6,4,2],
#                  [5,1,7],
#                  [9,3,3],
#                  [8,5,4]
#                  ])

# returned_array=sum_diff(matrix)
# print(returned_array)
# #This should print [-13, 1]

"""////Question 3////"""

# def find_apartment_names(grid):
#     """
#     Find potential apartment names by comparing characters on the primary diagonal
#     with their counterparts from top-left to bottom-right.
    
#     Args:
#         grid: A square 2D array of characters
        
#     Returns:
#         An array of mismatched characters found on the diagonal
#     """
#     n = len(grid)
#     apartment_names = []
    
#     # Compare the top-left to bottom-right diagonal elements
#     for i in range(n//2 + n%2):  # Iterate only up to the middle (inclusive)
#         # Compare element at position (i,i) with element at position (n-1-i, n-1-i)
#         top_left = grid[i][i]
#         bottom_right = grid[n-1-i][n-1-i]
        
#         if i == n-1-i:
#             # Middle element in odd-sized matrix - always add this to potential names
#             already_exists = False
#             for j in range(len(apartment_names)):
#                 if apartment_names[j] == top_left:
#                     already_exists = True
#                     break
            
#             if not already_exists:
#                 apartment_names.append(top_left)
#         elif top_left != bottom_right:
#             # Found a mismatch, both characters are potential apartment names
#             # Check if top_left is already in apartment_names
#             already_exists = False
#             for j in range(len(apartment_names)):
#                 if apartment_names[j] == top_left:
#                     already_exists = True
#                     break
            
#             if not already_exists:
#                 apartment_names.append(top_left)
            
#             # Check if bottom_right is already in apartment_names
#             already_exists = False
#             for j in range(len(apartment_names)):
#                 if apartment_names[j] == bottom_right:
#                     already_exists = True
#                     break
            
#             if not already_exists:
#                 apartment_names.append(bottom_right)
    
#     return apartment_names

# # Test case 1: 4x4 grid
# grid1 = [
#     ['A', 'D', 'M', 'Q'],
#     ['E', 'S', 'Y', 'K'],
#     ['J', 'F', 'O', 'L'],
#     ['P', 'X', 'J', 'A']
# ]

# print("Test Case 1:")
# for row in grid1:
#     for col in row:
#         print(col, end=" ")
#     print()

# apartments1 = find_apartment_names(grid1)
# print("Possible Apartment Names: ", end="")
# for apt in apartments1:
#     print(apt, end=" ")
# print("\n")

# # Test case 2: 5x5 grid
# grid2 = [
#     ['A', 'D', 'M', 'Q', 'F'],
#     ['E', 'S', 'Y', 'K', 'W'],
#     ['J', 'F', 'O', 'L', 'T'],
#     ['P', 'X', 'J', 'S', 'Y'],
#     ['V', 'R', 'K', 'G', 'P']
# ]

# print("Test Case 2:")
# for row in grid2:
#     for col in row:
#         print(col, end=" ")
#     print()

# apartments2 = find_apartment_names(grid2)
# print("Possible Apartment Names: ", end="")
# for apt in apartments2:
#     print(apt, end=" ")
# print()

# """////Question 5////"""
# """ n = len(matrix)
#     for i in range(n // 2):  # Loop through layers
#         for j in range(i, n - i - 1):  # Loop through elements in the current layer
#             # Perform a 4-way swap
#             temp = matrix[i][j]
#             matrix[i][j] = matrix[n - j - 1][i]
#             matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
#             matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
#             matrix[j][n - i - 1] = temp
#     return matrix"""
# def rotate_matrix(matrix):
#     row = len(matrix)
#     col = len(matrix[0])
#     for i in range(row):
#         for j in range(col):
#             if i < j:
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

#     for i in range(row):
#         for j in range(col//2):
#             temp=matrix[i][j]
#             matrix[i][j]=matrix[i][col-j-1]
#             matrix[i][col-j-1]=temp
#     return matrix

# # Sample Input
# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# matrix2 = [
#     [5, 1, 9, 11],
#     [2, 4, 8, 10],
#     [13, 3, 6, 7],
#     [15, 14, 12, 16]
# ]

# # Rotate matrices
# result1 = rotate_matrix(matrix1)
# result2 = rotate_matrix(matrix2)

# print(result1) # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
# print(result2) # Output: [[15,13,2,5], [14,3,4,1], [12,6,8,9], [16,7,10,11]]

# """////Question 6////"""

# def rotate_matrix(matrix):
#     row = len(matrix)
#     col = len(matrix[0])
#     for i in range(row):
#         for j in range(col):
#             if i < j:
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

#     for j in range(col):
#         for i in range(row//2):
#             temp=matrix[j][i]
#             matrix[j][i]=matrix[j][row-i-1]
#             matrix[j][row-i-1]=temp
#     return matrix

# # Sample Input
# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# matrix2 = [
#     [5, 1, 9, 11],
#     [2, 4, 8, 10],
#     [13, 3, 6, 7],
#     [15, 14, 12, 16]
# ]

# # Rotate matrices
# result1 = rotate_matrix(matrix1)
# result2 = rotate_matrix(matrix2)

# print(result1) # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
# print(result2) # Output: [[15,13,2,5], [14,3,4,1], [12,6,8,9], [16,7,10,11]]

"""////Question 7////"""

# def zig_zag(matrix):
#     n = len(matrix)  # Assuming square matrix (n x n)
#     result = ""
    
#     # Print upper triangle (including the main diagonal)
#     for i in range(n):
#         row = 0
#         col = i
        
#         while col >= 0 and row < n:
#             result += matrix[row][col] + " "
#             row += 1
#             col -= 1
    
#     # Print lower triangle (excluding the main diagonal)
#     for i in range(1, n):
#         row = i
#         col = n - 1
        
#         while row < n and col >= 0:
#             result += matrix[row][col] + " "
#             row += 1
#             col -= 1
    
#     print(result.strip())

# # Example usage with the given matrix
# matrix = [
#     ['D', 'B', 'G', 'S'],
#     ['A', 'G', 'T', 'S'],
#     ['W', 'U', 'R', 'N'],
#     ['O', 'H', 'R', 'O']
# ]

# zig_zag(matrix)  # Should print: D A B W G G O U T S H R S R N O


def zig_zag(matrix):
    n = len(matrix)  # Size of square matrix
    result = ""
    
    # Traverse all diagonals
    for diagonal_sum in range(2*n - 1):
        # Set starting position for current diagonal
        if diagonal_sum < n:
            row = diagonal_sum
            col = 0
        else:
            row = n - 1
            col = diagonal_sum - n + 1
        
        # Traverse current diagonal (moving up-right)
        while row >= 0 and col < n:
            result += matrix[row][col] + " "
            row = row - 1
            col = col + 1
    
    # Remove trailing space manually
    trimmed_result = ""
    for i in range(len(result) - 1):  # Skip last character if it's a space
        trimmed_result += result[i]
    
    print(trimmed_result)

# Example matrix from the problem
matrix = [
    ['D', 'B', 'G', 'S'],
    ['A', 'G', 'T', 'S'],
    ['W', 'U', 'R', 'N'],
    ['O', 'H', 'R', 'O']
]

zig_zag(matrix)