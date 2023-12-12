class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.key = self._get_min_value(node.right)
            node.right = self._delete_recursive(node.right, node.key)
        return node

    def _get_min_value(self, node):
        while node.left is not None:
            node = node.left
        return node.key

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

class PriorityQueue:
    def __init__(self):
        self.bst = BinarySearchTree()

    def insert(self, key):
        self.bst.insert(key)

    def delete(self, key):
        self.bst.delete(key)

    def search(self, key):
        node = self.bst.search(key)
        return node.key if node else None

pq = PriorityQueue()
pq.insert(15)
pq.insert(10)
pq.insert(20)
pq.insert(8)

print("탐색 결과:", pq.search(10))  
pq.delete(10)
print("10 삭제 후 탐색 결과:", pq.search(10))  
