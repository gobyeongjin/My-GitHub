class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def bubble_sort(self):
        end = None
        while end != self.head:
            p = self.head
            while p.next != end:
                q = p.next
                if p.data > q.data:
                    p.data, q.data = q.data, p.data
                p = p.next
            end = p


ll = LinkedList()
ll.add(4)
ll.add(2)
ll.add(3)
ll.add(1)

ll.bubble_sort()


current = ll.head
while current:
    print(current.data)
    current = current.next
