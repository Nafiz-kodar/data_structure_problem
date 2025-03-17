class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.prev = None

def create_doubly_linked_list(elements):
    dummy_head = Node(None)
    dummy_head.next = dummy_head
    dummy_head.prev = dummy_head
    tail = dummy_head
    for elem in elements:
        new_node = Node(elem)
        new_node.prev = tail
        new_node.next = dummy_head
        tail.next = new_node
        dummy_head.prev = new_node
        tail = new_node
    return dummy_head

def printList(dh):
    temp = dh.next
    while temp != dh:
        print(temp.elem, end=" -> ")
        temp = temp.next
    print("None")

def length(head):
    temp = head.next
    count = 0
    while temp != head:
        count += 1
        temp = temp.next
    return count

def Removes_client(head):
    temp = head.next
    len= length(head)
    while temp != head:
        next_node = temp.next
        if temp.elem % len == 0:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
        temp = next_node
    return head

# Driver code
elements = [17, 36 ,66,12, 66, 67]
dummy_head = create_doubly_linked_list(elements)

print("Original list:")
printList(dummy_head)

dummy_head = Removes_client(dummy_head)

print("List after removing clients:")
printList(dummy_head)


