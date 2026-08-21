# Delete the fist node

def delete_head(head):
    if head is None:
        return None

    if head.next is None:
        return None

    head = head.next
    current = head

    while current is not None:
        print(current.data)
        current = current.next
        
def delete_last(head):
    if head is None:
        return None

    if head.next is None:
        return None

    current = head

    while current.next.next is not None:
        current = current.next
        
    current.next = None
    return head

def delete_node(head, target):
    if head is None:
        return None
    
    if head.data == target:
        return None
    
    current = head
    while current.next is not None:
        if current.next.data == target:
            current.next = current.next.next
            return head

        current = current.next
    return head

def delete_all(head, target):
    while head is not None and head.data == target:
        head = head.next

    if head is None:
        return None

    current = head
    while current.next is not None:
        if current.next.data == target:
            current.next = current.next.next
        else:
            current = current.next

    return head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(30)
node6 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

head = node1

head = delete_all(head, 30)
current = head

while current is not None:
    print(current.data)
    current = current.next
