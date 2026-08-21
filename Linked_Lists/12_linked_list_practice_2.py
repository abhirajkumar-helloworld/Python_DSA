class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1
current = head

count = 0

while current is not None:
    count += 1
    current = current.next

print(count)

head = node1
current = head
found = False
target = 30

while current is not None:
    if current.data == target:
        print("Found")
        found = True
        break
    else:
        current = current.next

if not found:
    print("Not found")

class Node:
    def __init__(self1, data1):
        self1.data = data1
        self1.next = None

node5 = Node(10)
node6 = Node(5)
node7 = Node(90)
node8 = Node(20)

node5.next = node6
node6.next = node7
node7.next = node8

head1 = node5
current = head1
maximum = node5.data

while current is not None:
    if current.data > maximum:
        maximum = current.data

    current = current.next

print(f"Maximum = {maximum}")