import numpy as np

class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None

def createList(arr):
    if not arr.size:
        return None
    head = Node(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = Node(arr[i])
        cur = cur.next
    return head

def printLinkedList(head):
    cur = head
    while cur:
        print(cur.elem, end=" → ")
        cur = cur.next
    print("None")

def idGenerator(head1, head2, head3):
    # Reverse the first linked list
    prev = None
    cur = head1
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    reversed_head1 = prev

    # Create the first four nodes of the new linked list from the reversed first linked list
    new_head = None
    n_cur = None
    cur = reversed_head1
    count = 0
    while cur and count < 4:
        n_node = Node(cur.elem)
        if not new_head:
            new_head = n_node
            n_cur = n_node
        else:
            n_cur.next = n_node
            n_cur = n_node
        cur = cur.next
        count += 1

    # Add the remaining four digits by summing the elements of the second and third linked lists
    cur2 = head2
    cur3 = head3
    count = 0
    while cur2 and cur3 and count < 4:
        sum_digits = cur2.elem + cur3.elem
        new_digit = sum_digits % 10 if sum_digits >= 10 else sum_digits

        n_node = Node(new_digit)
        n_cur.next = n_node
        n_cur = n_node

        cur2 = cur2.next
        cur3 = cur3.next
        count += 1

    # Handle cases where either linked list is shorter than expected
    while count < 4:
        n_node = Node(0)
        n_cur.next = n_node
        n_cur = n_node
        count += 1

    return new_head

# Test cases (Assuming createList and printLinkedList are defined elsewhere)
print('==============Test Case 1=============')
head1 = createList(np.array([0,3,2,2]))
head2 = createList(np.array([5,2,2,1]))
head3 = createList(np.array([4,3,2,1]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)
print("Linked List 3:")
printLinkedList(head3)

result = idGenerator(head1, head2, head3)
print("New ID:")
printLinkedList(result)    #This should print  2 → 2 → 3 → 0 → 9 → 5 → 4 → 2


print('==============Test Case 2=============')
head1 = createList(np.array([0,3,9,1]))
head2 = createList(np.array([3,6,5,7]))
head3 = createList(np.array([2,4,3,8]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)
print("Linked List 3:")
printLinkedList(head3)

result = idGenerator(head1, head2, head3)
print("New ID:")
printLinkedList(result)    #This should print 1 → 9 → 3 → 0 → 5 → 0 → 8 → 5
