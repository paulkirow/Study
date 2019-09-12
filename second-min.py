def initOrAppend(dict, key, value):
    if key in dict:
        dict[key].append(value)
    else:
        dict[key] = [value]


def print_line(line, d):
    last_len = 0
    s = ''
    for i in range(len(line)):
        key = line[i]
        d_line = (d + 1 if i % len(line) != 0 else d)
        num_space = (d_line * (d_line - 1) + 1 - last_len) if d_line != 0 else 0
        s += ' ' * num_space + str(key)
        last_len = len(str(key)) - 1
    return s


class TreeNode:

    # Utility function to create a new tree node
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None

    def build_from_array(self, arr, d=0):
        if len(arr) == 0:
            return self
        if arr[d] is None:
            return None
        self.val = arr[d]
        newd = (d * 2) + 1
        if newd < len(arr):
            self.left = TreeNode.build_from_array(TreeNode(), arr, newd)
        if newd + 1 < len(arr):
            self.right = TreeNode.build_from_array(TreeNode(), arr, newd + 1)
        return self

    def __str__(self):
        d = self.getDepth(self) - 1
        result = {}
        s = ''
        self.print_tree_r(result, d)
        for k in result.keys():
            s += print_line(result[k], k)
            s += '\n'
        return s

    def getDepth(self, node):
        if node is None:
            return 0
        return 1 + max(self.getDepth(node.left), self.getDepth(node.right))

    def print_tree_r(self, result, d):
        if d < 0:
            return
        if d in result:
            result[d].append(self.val)
        else:
            result[d] = [self.val]
        if self.left is not None:
            self.left.print_tree_r(result, d - 1)
        else:
            d_ = d - 1
            k = 0
            while d_ >= 0:
                k += 1
                for i in range(2 ** k):
                    initOrAppend(result, d_, ' ')
                d_ -= 1

        if self.right is not None:
            self.right.print_tree_r(result, d - 1)
        else:
            d_ = d - 1
            k = 0
            while d_ >= 0:
                k += 1
                for i in range(2 ** k):
                    initOrAppend(result, d_, ' ')
                d_ -= 1


def findSecondMinimumValue(root: TreeNode) -> int:
    def findMin(node, minimum):
        if node is None:
            return minimum
        return min(node.val, findMin(node.left, minimum), findMin(node.right, minimum))

    def findSecondMin(node, min2, min1):
        if node is None:
            return min2
        leftm = findSecondMin(node.left, min2, min1)
        rightm = findSecondMin(node.right, min2, min1)
        if leftm == min1:
            leftm = node.val
        if rightm == min1:
            rightm = node.val
        this_min = min(node.val, leftm, rightm)
        return this_min

    if root is None:
        return -1

    min1 = findMin(root, root.val)
    min2 = findSecondMin(root, root.val, min1)
    return min2


tree = TreeNode()
tree.build_from_array(
    [1, "Two", "Three", 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
     'k'])
print(tree)

tree.build_from_array([2, 2, 5, None, None, 5, 7])
print(tree)
print("Second Min: " + str(findSecondMinimumValue(tree)))
