class BinaryNode:

    # Utility function to create a new tree node
    def __init__(self):
        self.key = None
        self.left = None
        self.right = None

    def build_from_array(self, arr, d=0):
        if len(arr) == 0:
            return self
        self.key = arr[d]
        newd = (d*2)+1
        if newd < len(arr):
            self.left = BinaryNode.build_from_array(BinaryNode(),arr, newd)
        if newd+1 < len(arr):
            self.right = BinaryNode.build_from_array(BinaryNode(), arr, newd + 1)
        return self

    def __str__(self):
        d = self.get_depth()
        result = {}
        s = ''
        self.print_tree_r(result, d)
        for k in result.keys():
            s += self.print_line(result[k], k)
            s += '\n'
        return s

    def print_line(self, line, d):
        last_len = 0
        s = ''
        for i in range(len(line)):
            key = line[i]
            d_line = (d+1 if i % len(line)!=0 else d)
            num_space = (d_line * (d_line - 1) + 1 - last_len) if d_line != 0 else 0
            s += ' ' * num_space + str(key)
            last_len = len(str(key)) - 1
        return s

    def print_tree_r(self, result, d):
        if (d<0):
            return
        if (d in result):
            result[d].append(self.key)
        else:
            result[d] = [self.key]
        if self.left is not None:
            self.left.print_tree_r(result, d - 1)
        if self.right is not None:
            self.right.print_tree_r(result, d - 1)

    def get_depth(self):
        left = self.left
        d = 0
        while left is not None:
            left = left.left
            d+=1
        return d

class NryNode:

    # Utility function to create a new tree node
    def __init__(self, key):
        self.key = key
        self.child = []


tree = BinaryNode()
tree.build_from_array([1,"Two","Three",4,5,6,7,8,9,10,11,12,13,14,15,'a','b','c','d','e','f','g','h','i','j','k'])
print(tree)