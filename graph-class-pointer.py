class Node:
    value = None
    pointers = []

    def __init__(self):
        pass

    def __init__(self, value):
        self.value = value

    def __init__(self, value, pointers):
        self.value = value
        self.pointers = pointers

class Pointer:
    weight = None

root = Node(5)
n1 = Node(1)
n2 = Node(20)
n3 = Node(14)
n4 = Node(7)

root.pointers = [n1,n2]
n2.pointers = [n3]
n2.pointers = [n3]

