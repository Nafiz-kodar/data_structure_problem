

class Node:
    def __init__(self, elem, next=None):
        self.elem, self.next = elem, next


def createList(arr):
    head = Node(arr[0])
    tail = head
    for i in range(1, len(arr)):
        newNode = Node(arr[i])
        tail.next = newNode
        tail = newNode
    return head


def printLinkedList(head):
    temp = head
    while temp is not None:
        if temp.next is not None:
            print(temp.elem, end='-->')
        else:
            print(temp.elem)
        temp = temp.next
    print()


def count(head):
    count = 0
    temp = head
    while temp is not None:
        count += 1
        temp = temp.next
    return count


def nodeAt(head, idx):
    temp = head
    for i in range(idx):
        if temp is None:  
            return None
        temp = temp.next
    if temp:
        return temp.elem
    return None  


def word_Decoder(head):
    num = 13 % count(head)
    d_head = Node(None)  
    tail = d_head

    for i in range(1, count(head)):  # Start from 1 to skip the 0 indexed element
        if i % num == 0:
            new_node = Node(nodeAt(head, i))
            tail.next = new_node
            tail = new_node

    # Reverse the linked list starting from the node after the dummy head
    prev = None
    cur = d_head.next
    while cur is not None:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node

    d_head.next = prev  # Set the new head's next to the reversed list's head
    return d_head  # Return the dummy head as the new head of the reversed linked list

head = createList(['B', 'M', 'D', 'T', 'N', 'O', 'A', 'P', 'S', 'C'])
#Driver Code
print('==============Test Case 1=============')
head = createList(['B', 'M', 'D', 'T', 'N', 'O', 'A', 'P', 'S', 'C'])
print("Encoded Word:")
printLinkedList(head) #This should print B→M→D→T→N→O→A→P→S→C

result = word_Decoder(head)
print("Decoded Word:")
printLinkedList(result)    #This should print None→C→A→T
head = createList(['Z', 'O', 'T', 'N', 'X'])
print('==============Test Case 2=============')

head = createList(['Z', 'O', 'T', 'N', 'X'])
print("Encoded Word:")
printLinkedList(head) #This should print Z→O→T→N→X

result = word_Decoder(head)
print("Decoded Word:")
printLinkedList(result)    #This should print None→N