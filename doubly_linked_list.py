# class Node:
#     def __init__(self, elem):
#         self.elem = elem
#         self.next = None
#         self.prev = None

# # def create_doubly_linked_list(elements):
# #     dummy_head = Node(None)
# #     dummy_head.next = dummy_head
# #     dummy_head.prev = dummy_head
# #     tail = dummy_head
# #     for elem in elements:
# #         new_node = Node(elem)
# #         new_node.prev = tail
# #         new_node.next = dummy_head
# #         tail.next = new_node
# #         dummy_head.prev = new_node
# #         tail = new_node
# #     return dummy_head

# # def printList(dh):
# #     temp = dh.next
# #     while temp != dh:
# #         print(temp.elem, end=" -> ")
# #         temp = temp.next
# #     print("None")

# # def length(head):
# #     temp = head.next
# #     count = 0
# #     while temp != head:
# #         count += 1
# #         temp = temp.next
# #     return count

# # #///Question 2////#

# # def Removes_client(head):
# #     temp = head.next
# #     len= length(head)
# #     while temp != head:
# #         if temp.elem % len == 0:
# #             temp.prev.next = temp.next
# #             temp.next.prev = temp.prev
# #         temp = temp.next
# #     return head

# # # Driver code
# # elements = [17, 36 ,66,12, 66, 67]
# # dummy_head = create_doubly_linked_list(elements)

# # print("Original list:")
# # printList(dummy_head)

# # dummy_head = Removes_client(dummy_head)

# # print("List after removing clients:")
# # printList(dummy_head)

# #///Question 4////#

# # def insert_list(head_X, head_A, k):
# #     # Check if k is valid
# #     if k < 0:
# #         return head_X  # Invalid index, return original list
    
# #     # Handle special case: if k is 0, insert at the beginning
# #     if k == 0:
# #         # Find the current last node of list A
# #         temp_A = head_A
# #         last_A = None
# #         while temp_A:
# #             last_A = temp_A
# #             temp_A = temp_A.next
        
# #         # If list A is empty, return original list X
# #         if not last_A:
# #             return head_X
        
# #         # Connect the last node of A to the first node of X
# #         last_A.next = head_X.next
        
# #         # Connect the first node of X's prev to the last node of A
# #         if head_X.next:
# #             head_X.next.prev = last_A
        
# #         # Connect the dummy head to the first node of A
# #         head_X.next = head_A
        
# #         # Set the prev of the first node of A to the dummy head
# #         head_A.prev = head_X
        
# #         return head_X
    
# #     # For any other k, find the k-th position
# #     current = head_X
# #     pos = 0
    
# #     # Traverse to the k-th position
# #     while current.next != head_X and pos < k:
# #         current = current.next
# #         pos += 1
    
# #     # If k is beyond the length of X, append A at the end
# #     if pos >= k:
# #         current = head_X.prev  # The last node of X
    
# #     # Now current is the node after which we need to insert list A
    
# #     # Find the last node of list A
# #     temp_A = head_A
# #     last_A = None
# #     while temp_A:
# #         last_A = temp_A
# #         temp_A = temp_A.next
    
# #     # If list A is empty, return original list X
# #     if not last_A:
# #         return head_X
    
# #     # Get the next node after current
# #     next_node = current.next
    
# #     # Connect current to the head of A
# #     current.next = head_A
# #     head_A.prev = current
    
# #     # Connect the last node of A to the next node
# #     last_A.next = next_node
    
# #     # Update the prev of the next node
# #     if next_node:
# #         next_node.prev = last_A
    
# #     return head_X

# # # Helper function to create a dummy headed doubly circular linked list
# # def create_doubly_circular_list(elements):
# #     dummy_head = Node("DH")  # Dummy head with "DH" as element
# #     dummy_head.next = dummy_head
# #     dummy_head.prev = dummy_head
    
# #     current = dummy_head
# #     for elem in elements:
# #         new_node = Node(elem)
# #         new_node.prev = current
# #         new_node.next = dummy_head
# #         current.next = new_node
# #         dummy_head.prev = new_node
# #         current = new_node
        
# #     return dummy_head

# # # Helper function to create a singly linked list
# # def create_singly_list(elements):
# #     if not elements:
# #         return None
    
# #     head = Node(elements[0])
# #     current = head
    
# #     for elem in elements[1:]:
# #         current.next = Node(elem)
# #         current = current.next
        
# #     return head

# # # Helper function to print a doubly circular linked list
# # def print_doubly_circular(head):
# #     result = ["DH"]
# #     current = head.next
    
# #     while current != head:
# #         result.append(str(current.elem))
# #         current = current.next
        
# #     return " ⟷ ".join(result)

# # # Helper function to print a singly linked list
# # def print_singly(head):
# #     result = []
# #     current = head
    
# #     while current:
# #         result.append(str(current.elem))
# #         current = current.next
        
# #     return " -> ".join(result)

# # # Test case 1
# # X1 = create_doubly_circular_list([2, 3, 1, 9])
# # A1 = create_singly_list([4, 8])
# # k1 = 2

# # print("Sample Input 1:")
# # print(f"X = {print_doubly_circular(X1)}")
# # print(f"A = {print_singly(A1)}")
# # print(f"k = {k1}")

# # result1 = insert_list(X1, A1, k1)

# # print("\nSample Output 1:")
# # print(print_doubly_circular(result1))

# # # Test case 2
# # X2 = create_doubly_circular_list([2, 3, 1, 9])
# # A2 = create_singly_list([5, 4, 6])
# # k2 = 0

# # print("\nSample Input 2:")
# # print(f"X = {print_doubly_circular(X2)}")
# # print(f"A = {print_singly(A2)}")
# # print(f"k = {k2}")

# # result2 = insert_list(X2, A2, k2)

# # print("\nSample Output 2:")
# # print(print_doubly_circular(result2))

# # #//// Question 7////

# class DoublyNode:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#         self.prev = None

# def createDLL(values):
#     """
#     Create a dummy headed circular doubly linked list from a list of values.
    
#     Args:
#         values: List of values to create nodes from
        
#     Returns:
#         head: The dummy head node of the created list
#     """
#     # Create a dummy head
#     head = DoublyNode("Head")
#     head.next = head
#     head.prev = head
    
#     if not values:
#         return head
    
#     # Initialize with the first real node
#     current = DoublyNode(values[0])
#     current.prev = head
#     current.next = head
#     head.next = current
#     head.prev = current
    
#     # Add the rest of the nodes
#     last = current
#     for value in values[1:]:
#         current = DoublyNode(value)
#         current.prev = last
#         current.next = head
#         last.next = current
#         head.prev = current
#         last = current
        
#     return head

# def printDLL(head):
#     """
#     Print the values in a dummy headed circular doubly linked list.
    
#     Args:
#         head: The dummy head node of the list
        
#     Returns:
#         A string representation of the list
#     """
#     if head.next == head:
#         return "Empty list"
        
#     result = []
#     current = head.next
    
#     while current != head:
#         result.append(str(current.value))
#         current = current.next
        
#     return " ⇄ ".join(result)

# def getNodeByValue(head, value):
#     """
#     Find a node with the given value in the list.
    
#     Args:
#         head: The dummy head node of the list
#         value: The value to search for
        
#     Returns:
#         The node containing the value, or None if not found
#     """
#     if head.next == head:
#         return None
        
#     current = head.next
    
#     while current != head:
#         if current.value == value:
#             return current
#         current = current.next
        
#     return None

# # The reverseDLLBetweenTwoValues function should be implemented here
# def reverseDLLBetweenTwoValues(head, x, y):
#     temp = head.next
#     start = None
#     end = None
    
#     # Find the start node
#     while temp != head:
#         if temp.value == x:
#             start = temp
#             break
#         temp = temp.next
    
#     # If start node is not found, return the original list
#     if not start:
#         return head
    
#     # Find the end node
#     temp = head.next
#     while temp != head:
#         if temp.value == y:
#             end = temp
#             break
#         temp = temp.next
    
#     # If end node is not found, return the original list
#     if not end:
#         return head
    
#     # Reverse the values between start and end
#     while start != end and start.prev != end:
#         start.value, end.value = end.value, start.value
#         start = start.next
#         end = end.prev
    
#     return head
    
# # Driver code
# if __name__ == "__main__":
#     # Sample function call from the question
#     values = [10, 20, 30, 90, 40, 50]
#     head = createDLL(values)
#     x = 20
#     y = 40
    
#     print("Sample Function Call:")
#     print(f"head => {printDLL(head)},")
#     print(f"x = {x}, y = {y}")
#     re=reverseDLLBetweenTwoValues(head, x, y)
#     print(f"head => {printDLL(re)}")
    
#     # The result after calling the function would be displayed here
#     # For now, we'll just print the expected result
#     print("\nSample Returned Result:")
#     print("Head of the modified linked list =>")
#     print("10 ⇄ 40 ⇄ 90 ⇄ 30 ⇄ 20 ⇄ 50")

# #////Question 8////

# # class Node:
# #     def __init__(self, elem):
# #         self.elem = elem
# #         self.next = None
# #         self.prev = None

# # def create_doubly_linked_list(elements):
# #     """
# #     Create a doubly linked list from a list of elements.
    
# #     Args:
# #         elements: List of integers to create nodes from
        
# #     Returns:
# #         head: The head node of the created list
# #     """
# #     if not elements:
# #         return None
    
# #     # Create the head node
# #     head = Node(elements[0])
# #     current = head
    
# #     # Create the rest of the nodes
# #     for elem in elements[1:]:
# #         new_node = Node(elem)
# #         new_node.prev = current
# #         current.next = new_node
# #         current = new_node
        
# #     return head

# # def print_doubly_linked_list(head):
# #     """
# #     Print a doubly linked list in the format specified in the problem.
    
# #     Args:
# #         head: The head node of the list
        
# #     Returns:
# #         A string representation of the list
# #     """
# #     if not head:
# #         return "Empty list"
        
# #     result = []
# #     current = head
    
# #     while current:
# #         result.append(str(current.elem))
# #         current = current.next
        
# #     return " ⇄ ".join(result)

# # def is_odd(num):
# #     """
# #     Check if a number is odd.
    
# #     Args:
# #         num: The number to check
        
# #     Returns:
# #         True if the number is odd, False otherwise
# #     """
# #     return num % 2 != 0

# # def count_odd_elements(head):
# #     """
# #     Count the number of odd elements in the list.
    
# #     Args:
# #         head: The head node of the list
        
# #     Returns:
# #         The count of odd elements
# #     """
# #     count = 0
# #     current = head
    
# #     while current:
# #         if is_odd(current.elem):
# #             count += 1
# #         current = current.next
        
# #     return count

# # def get_tail(head):
# #     """
# #     Get the tail node of the list.
    
# #     Args:
# #         head: The head node of the list
        
# #     Returns:
# #         The tail node of the list
# #     """
# #     if not head:
# #         return None
        
# #     current = head
# #     while current.next:
# #         current = current.next
        
# #     return current

# # # The main function to rearrange the list should be implemented here
# # def rearrange_odd_even(head):
# #     """
# #     Rearrange the doubly linked list so that all odd elements appear before all even elements
# #     while maintaining the relative order.
    
# #     Args:
# #         head: The head node of the list
        
# #     Returns:
# #         The head node of the rearranged list
# #     """
# #     # Your implementation here
# #     pass

# # # Driver code to test the functions
# # def test_helpers():
# #     # Test case 1: [5, 2, 8, 1, 4, 7]
# #     elements1 = [5, 2, 8, 1, 4, 7]
# #     head1 = create_doubly_linked_list(elements1)
# #     print(f"Original list 1: {print_doubly_linked_list(head1)}")
# #     print(f"Odd elements count: {count_odd_elements(head1)}")
# #     print(f"Is 5 odd? {is_odd(5)}")
# #     print(f"Is 2 odd? {is_odd(2)}")
# #     tail1 = get_tail(head1)
# #     print(f"Tail element: {tail1.elem}")
    
# #     # Test case 2: [7, 9, 2, 4]
# #     elements2 = [7, 9, 2, 4]
# #     head2 = create_doubly_linked_list(elements2)
# #     print(f"\nOriginal list 2: {print_doubly_linked_list(head2)}")
    
# #     # Test case 3: [6, 2, 8, 10, 12]
# #     elements3 = [6, 2, 8, 10, 12]
# #     head3 = create_doubly_linked_list(elements3)
# #     print(f"\nOriginal list 3: {print_doubly_linked_list(head3)}")

# # def run_examples():
# #     # Example 1
# #     print("Example 1:")
# #     elements1 = [5, 2, 8, 1, 4, 7]
# #     head1 = create_doubly_linked_list(elements1)
# #     print(f"Input: {print_doubly_linked_list(head1)}")
# #     # After implementing rearrange_odd_even, uncomment the following lines
# #     # result1 = rearrange_odd_even(head1)
# #     # print(f"Output: {print_doubly_linked_list(result1)}")
# #     print("Expected output: 5 ⇄ 1 ⇄ 7 ⇄ 2 ⇄ 8 ⇄ 4")
    
# #     # Example 2
# #     print("\nExample 2:")
# #     elements2 = [7, 9, 2, 4]
# #     head2 = create_doubly_linked_list(elements2)
# #     print(f"Input: {print_doubly_linked_list(head2)}")
# #     # After implementing rearrange_odd_even, uncomment the following lines
# #     # result2 = rearrange_odd_even(head2)
# #     # print(f"Output: {print_doubly_linked_list(result2)}")
# #     print("Expected output: 7 ⇄ 9 ⇄ 2 ⇄ 4")
    
# #     # Example 3
# #     print("\nExample 3:")
# #     elements3 = [6, 2, 8, 10, 12]
# #     head3 = create_doubly_linked_list(elements3)
# #     print(f"Input: {print_doubly_linked_list(head3)}")
# #     # After implementing rearrange_odd_even, uncomment the following lines
# #     # result3 = rearrange_odd_even(head3)
# #     # print(f"Output: {print_doubly_linked_list(result3)}")
# #     print("Expected output: 6 ⇄ 2 ⇄ 8 ⇄ 10 ⇄ 12")

# # if __name__ == "__main__":
# #     # Uncomment the function you want to run
# #     # test_helpers()
# #     run_examples()


#////Question 11////

# Node class
class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.prev = None

# Solution function
def findPair(head, target):
    # Edge case: empty list or list with only one node
    if head is None or head.next == head:
        return None
    
    front = head.next  # Start from the first real node
    back = head.prev   # Start from the last node
    
    # Continue until pointers cross or meet
    while front != back and back.next != front:
        current_sum = front.elem + back.elem
        
        if current_sum == target:
            # Found a pair
            return (front, back)
        elif current_sum < target:
            # Sum is too small, move front pointer forward
            front = front.next
        else:
            # Sum is too large, move back pointer backward
            back = back.prev
    
    # No pair found
    return None

# Helper function to create a circular doubly linked list
def create_circular_doubly_linked_list(values):
    if not values:
        return None
    
    # Create dummy head
    dummy_head = Node(0)
    dummy_head.next = dummy_head
    dummy_head.prev = dummy_head
    
    tail = dummy_head
    
    # Add values to the list
    for val in values:
        new_node = Node(val)
        
        # Connect new_node to the list
        new_node.prev = tail
        new_node.next = dummy_head
        
        # Update connections
        tail.next = new_node
        dummy_head.prev = new_node
        
        # Move tail
        tail = new_node
    
    return dummy_head

# Helper function to print the result
def print_result(result):
    if result is None:
        print("None")
    else:
        print(f"({result[0].elem}, {result[1].elem})")

# Driver code for testing
if __name__ == "__main__":
    # Test case 1: DH ↔ 1 ↔ 2 ↔ 3 ↔ 4 ↔ 6 ↔ 8 ↔ 9, Target: 10
    values1 = [1, 2, 3, 4, 6, 8, 9]
    head1 = create_circular_doubly_linked_list(values1)
    result1 = findPair(head1, 10)
    print("Test case 1:", end=" ")
    print_result(result1)
    
    # Test case 2: DH ↔ 1 ↔ 3 ↔ 5 ↔ 7 ↔ 9 ↔ 10, Target: 12
    values2 = [1, 3, 5, 7, 9, 10]
    head2 = create_circular_doubly_linked_list(values2)
    result2 = findPair(head2, 12)
    print("Test case 2:", end=" ")
    print_result(result2)
    
    # Test case 3: DH ↔ 1 ↔ 2 ↔ 4 ↔ 5 ↔ 7, Target: 20
    values3 = [1, 2, 4, 5, 7]
    head3 = create_circular_doubly_linked_list(values3)
    result3 = findPair(head3, 20)
    print("Test case 3:", end=" ")
    print_result(result3)
    
    # Test case 4: Empty list, Target: 20
    head4 = create_circular_doubly_linked_list([])
    result4 = findPair(head4, 20)
    print("Test case 4:", end=" ")
    print_result(result4)
