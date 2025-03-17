# Description: This file has the implementation of singly linked list.

#Node class

class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None

#Creating a linked list
def createList(arr):
    head = Node(arr[0])
    tail = head
    for i in range(1, len(arr)):
        newNode = Node(arr[i])
        tail.next = newNode
        tail = newNode
    return head
    
#Printing linked list
def printList(head):
    temp = head
    while temp != None:
        if temp.next != None:
            print(temp.elem, end = '-->')
        else:
            print(temp.elem)
        temp = temp.next
    print()

#Retrieving element from an index

def elem_at(head, idx):
    temp = head
    count = 0
    while temp != None:
        if count == idx:
            return temp.elem
        count += 1
        temp = temp.next


#Retrieving node from an index

def node_at(head, idx):
    temp = head
    count = 0
    while temp != None:
        if count==idx:
            return temp
        count += 1
        temp = temp.next
    return "Index out of range"
        
# #//// question 2 ////
# def isSumPossible(head,n):
#     temp=head
#     while temp!=None:
#         temp1=temp.next
#         while temp1!=None:
#             if temp.elem+temp1.elem==n:
#                 return True
#             temp1=temp1.next
#         temp=temp.next
#     return False

# #//// question 3 ////
# def remove_Duplicates(head):   
#     temp=head
#     while temp!=None:
#         temp1=temp.next
#         while temp1!=None:
#             if temp.elem==temp1.elem:
#                 temp.next=temp1.next
#             temp1=temp1.next
#         temp=temp.next
#     return temp

# #//// question 4 //// ->->->->->->->->->-> need review
# def reverse_and_swap(head, i):
#     if head is None or i < 0:
#         return head

#     # Reverse the first part of the list up to the i
#     prev = None
#     current = head
#     count = 0
#     while current is not None and count < i:
#         next_node = current.next
#         current.next = prev
#         prev = current
#         current = next_node
#         count += 1

#     # If the i is out of range, return the reversed list
#     if current is None:
#         return prev

#     # The current node is the start of the second part
#     second_part_head = current

#     # Find the tail of the second part
#     while current.next is not None:
#         current = current.next

#     # Connect the tail of the second part to the reversed first part
#     current.next = prev

#     return second_part_head
#     # Driver code to test the reverse_and_swap function


#     # Create a linked list from an array
# arr = [1, 2, 3, 4, 5,6,7,8,9]
# head = createList(arr)

# # Print the original list
# print("Original list:")
# printList(head)

# # Reverse and swap the list at i 2
# i = 5
# new_head = reverse_and_swap(head, i)

# # Print the modified list
# print(f"Modified list after reversing and swapping at i {i}:")
# printList(new_head)


#//// question 20 ////
def rearrangeNodes(head,x):
    prev=None
    current_head=head
    temp=head
    while temp!=None:
        if temp.elem<=x:
            prev=temp
            temp=temp.next
        elif temp.elem>x:
            if temp.elem>current_head.elem:
                t=temp
                if prev is not None:
                    prev.next = temp.next
                else:
                    head = temp.next
                temp.next=current_head
                current_head=t
                temp=prev.next
            else:
                s=current_head.next
                current_head.next=temp
                temp.next=s

    
    return current_head


            # Driver code to test the rearrangeNodes function

# Create a linked list from an array
arr = [3, 5, 8, 5, 10, 2, 1]
head = createList(arr)

# Print the original list
print("Original list:")
printList(head)

# Rearrange nodes with x = 5
x = 5
new_head = rearrangeNodes(head, x)

# Print the modified list
print(f"Modified list after rearranging nodes with x = {x}:")
printList(new_head)
# Driver code to test the rearrangeNodes function

# Create a linked list from an array
arr = [2,3,9,4,2,7,5,3,6]
head = createList(arr)

# Print the original list
print("Original list:")
printList(head)

# Rearrange nodes with x = 3
x = 3
new_head = rearrangeNodes(head, x)

# Print the modified list
print(f"Modified list after rearranging nodes with x = {x}:")
printList(new_head)