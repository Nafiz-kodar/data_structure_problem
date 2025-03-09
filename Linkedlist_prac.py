import numpy as np

class Node:
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

    def createlist(arr):
        head=Node(arr[0])
        tail=head
        for i in range(1,len(arr)):
            newNode=Node(arr[i])
            tail.next=newNode
            tail=newNode
        return head

    def printList(head):
        temp = head
        while temp != None:
            if temp.next != None:
                print(temp.elem, end = '-->')
            else:
                print(temp.elem)
            temp = temp.next
        print()

    def iterate(head):
        temp=head
        count=0
        while temp!=None:
            #print(temp.elem)
            count+=1
            temp=temp.next
            
        return count
            
a=np.array([10,12,32,432,544,32])
#print(a)
print(Node.iterate(Node.createlist(a)))
