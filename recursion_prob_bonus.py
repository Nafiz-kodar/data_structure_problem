### HOMEWORK ON RECURSION ###

"TASK-01"
def remove_x(string):
    if string == "":
        return ""
    if string[0] == "x":
        return remove_x(string[1:])
    else:
        return string[0] + remove_x(string[1:])

# Test cases
print(remove_x("xabcx"))  # Output: "abc"
print(remove_x("x2x"))     # Output: ""
print(remove_x("abc"))    # Output: "abc"
print(remove_x("x3"))      # Output: ""
print(remove_x("xaxb"))   # Output: "ab"


"TASK-02"
def sumDigits(n):
    if n == 0:
        return 0
    else:
        right_digit = n % 10
        remaining=n//10
        return right_digit+sumDigits(remaining)
# Test cases
print(sumDigits(126))   
print(sumDigits(49))  
print(sumDigits(12)) 

"TASK-03"
def strCopies(string, sub, N):
    ans= helper(string, sub, N, 0)
    if ans == N:
        print (True)
    else:
        print (False)
def helper(string, sub, N, count):
        x=len(sub)
        if len(string) < x:
            return count
        if string[0:x] == sub:
            count += 1
        return helper(string[1:], sub, N, count)

# Test cases
strCopies("catcowcat", "cat", 2) 
strCopies("catcowcat", "cow", 2) 
strCopies("catcowcat", "cow", 1) 

"TASK-04"

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# def findMax_recursive(head):
#     if head is None:
#         return float('-inf')  # Return negative infinity if the list is empty
#     return max(head.value, findMax_recursive(head.next))

# # Helper function to create a linked list from a list
# def create_linked_list(values):
#     if not values:
#         return None
#     head = Node(values[0])
#     current = head
#     for value in values[1:]:
#         current.next = Node(value)
#         current = current.next
#     return head

# # Test cases
# head = create_linked_list([1, 5, 3, 9, 2])
# print(findMax_recursive(head))  # Output: 9

# head = create_linked_list([-10, -20, -30])
# print(findMax_recursive(head))  # Output: -10

# head = create_linked_list([])
# print(findMax_recursive(head))  # Output: -inf