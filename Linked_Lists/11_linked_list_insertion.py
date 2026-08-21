# insert at the beginning

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

head = node1

new_node = Node(5)
new_node.next = head
head = new_node

current = head


while current is not None:
    print(current.data)
    current = current.next

print("------------------------------------------------------")

# insert at the end

class Node:
    def __init__(self, data1):
        self.data = data1
        self.next = None

node4 = Node(10)
node5 = Node(20)
node6 = Node(30)

node4.next = node5
node5.next = node6

head1 = node4

new_node1 = Node(40)

current1 = head1

while current1.next is not None:
    current1 = current1.next

current1.next = new_node1

head1 = node4

current1 = head1

while current1 is not None:
    print(current1.data)
    current1 = current1.next