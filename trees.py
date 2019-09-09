import queue


class BinaryNode:

    # Utility function to create a new tree node
    def __init__(self):
        self.key = None
        self.left = None
        self.right = None

    def build_from_array(self, arr, d=0):
        if len(arr) == 0:
            return self
        if arr[d] == None:
            return None
        self.key = arr[d]
        newd = (d * 2) + 1
        if newd < len(arr):
            self.left = BinaryNode.build_from_array(BinaryNode(), arr, newd)
        if newd + 1 < len(arr):
            self.right = BinaryNode.build_from_array(BinaryNode(), arr, newd + 1)
        return self

    def __str__(self):
        d = self.getDepth(self) - 1
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
            d_line = (d + 1 if i % len(line) != 0 else d)
            num_space = (d_line * (d_line - 1) + 1 - last_len) if d_line != 0 else 0
            s += ' ' * num_space + str(key)
            last_len = len(str(key)) - 1
        return s

    def print_tree_r(self, result, d):
        if (d < 0):
            return
        if (d in result):
            result[d].append(self.key)
        else:
            result[d] = [self.key]
        if self.left is not None:
            self.left.print_tree_r(result, d - 1)
        else:
            d_ = d - 1
            k = 0
            while d_ >= 0:
                k += 1
                for i in range(2 ** k):
                    self.initOrAppend(result, d_, ' ')
                d_ -= 1

        if self.right is not None:
            self.right.print_tree_r(result, d - 1)
        else:
            d_ = d - 1
            k = 0
            while d_ >= 0:
                k += 1
                for i in range(2 ** k):
                    self.initOrAppend(result, d_, ' ')
                d_ -= 1

    def initOrAppend(self, dict, key, value):
        if key in dict:
            dict[key].append(value)
        else:
            dict[key] = [value]

    def isBalanced(self, root) -> bool:
        return self.isBalancedR(root) > -1

    def isBalancedR(self, node):
        if node is None:
            return 0
        leftH = self.isBalancedR(node.left)
        if leftH == -1:
            return -1
        rightH = self.isBalancedR(node.right)
        if rightH == -1:
            return -1

        if abs(leftH - rightH) > 1:
            return -1

        return max(leftH, rightH) + 1

    def isBalancedBad(self, root) -> bool:

        if root is None:
            return True

        leftDepth = 0
        if root.left is not None:
            leftDepth = self.getDepth(root.left)

        rightDepth = 0
        if root.right is not None:
            rightDepth = self.getDepth(root.right)

        if abs(leftDepth - rightDepth) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getDepth(self, node):
        if node is None:
            return 0
        return 1 + max(self.getDepth(node.left), self.getDepth(node.right))

    def constructMaximumBinaryTree(self, nums: [int]):
        return self.constructMaximumBinaryTreeR(nums)

    def constructMaximumBinaryTreeR(self, nums):
        if len(nums) == 0:
            return None
        m = self.getMaxIndex(nums)
        result = BinaryNode()
        result.key = nums[m]
        result.left = self.constructMaximumBinaryTreeR(nums[0:m])
        result.right = self.constructMaximumBinaryTreeR(nums[m + 1:len(nums)])
        return result

    def getMaxIndex(self, nums):
        m = 0
        for i in range(len(nums)):
            if nums[i] > nums[m]:
                m = i
        return m

    def flattenR(self, node):
        if node is None:
            return None

        flat_left_end = node
        if node.left is not None:
            flat_left_end = self.flattenR(node.left)

        flat_right_end = flat_left_end
        if node.right is not None:
            flat_right_end = self.flattenR(node.right)

        node.left, node.right, flat_left_end.right = None, node.left, node.right

        print(node.key)
        return flat_right_end

    def dfs_search(self, root, val):
        # Left Root Right
        result = None
        if root is None:
            return result

        if root.left is not None:
            result = self.dfs_search(root.left, val)

        if root.key == val:
            return root

        if result is None and root.right is not None:
            result = self.dfs_search(root.right, val)

        return result

    def bfs_search(self, root, val):
        if root.key == val:
            return root
        q = queue.Queue()
        q.put(root.left)
        q.put(root.right)
        while not q.empty():
            node = q.get()
            if node.key == val:
                return node
            q.put(node.left)
            q.put(node.right)
        return None


class NryNode:

    # Utility function to create a new tree node
    def __init__(self, key):
        self.key = key
        self.child = []


tree = BinaryNode()
tree.build_from_array(
    [1, "Two", "Three", 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
     'k'])
print("Is balanced: " + str(tree.isBalanced(tree)))
print("search 5: " + str(tree.dfs_search(tree, 5)))
print("search 11: " + str(tree.bfs_search(tree, 11)))
print(tree)

tree.build_from_array([1, 2, 2, 3, 3, None, None, 4, 4])
print("Is balanced: " + str(tree.isBalanced(tree)))
print(tree)

tree.build_from_array([1, None, 2, None, None, None, 3])
print("Is balanced: " + str(tree.isBalanced(tree)))
print(tree)
timedict = {}

tree.build_from_array([1, 2, 2, 3, 3, None, None, 4, 4])
print("Is balanced: " + str(tree.isBalanced(tree)))
print(tree)

tree = BinaryNode.constructMaximumBinaryTree(tree, [3, 2, 1, 6, 0, 5])
print(tree)

tree = BinaryNode.build_from_array(tree, [1, 2, None, 3])
print("Original")
print(tree)
BinaryNode.flattenR(tree, tree)
print("Flat")
print(tree)
