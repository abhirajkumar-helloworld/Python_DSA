def search(head, target):
    index = 0
    if head is None:
        return -1

    current = head

    while current is not None:
        if current.data == target:
            return index
        current = current.next
        index += 1

    return -1

def search_all(head, target):
    if head is None:
        return None

    result = []
    index = 0

    current = head

    while current is not None:
        if current.data == target:
            result.append(index)
        current = current.next
        index += 1

    return result

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
target = 99
index = search(head, target)

result = search_all(head, target)

if len(result) > 0:
    print(f"Target {target} found {len(result)} times")

else:
    print("Not found")