from node_creation import *


def nodeat(head,idx):
    count=0
    temp=head
    while temp is not None:
        if count==idx:
            return temp.elem
        count+=1
        temp=temp.next
    

def sum_dist(head, arr):
    sum=0
    for i in range(len(arr)):
        if nodeat(head, arr[i]) is not None:
            sum+=nodeat(head, arr[i])
    return sum


#[DO NOT MODIFY THE TESTER CODES BELOW]
#[THERE WILL BE 50% PENALTY IF IT'S MODIFIED]
print('==============Test Case 1=============')
LL1 = createList(np.array([10,16,-5,9,3,4]))
dist = np.array([2,0,5,2,8])
returned_value = sum_dist(LL1, dist)
print(f'Sum of Nodes: {returned_value}') #This should print Sum of Nodes: 4
#unittest.output_test(returned_value, 4)
print()