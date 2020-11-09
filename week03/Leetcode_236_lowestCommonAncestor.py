class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left and not right:
            return
        if not left:
            return right
        if not right:
            return left

        return root

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree(object):
    lis = []

    def __init__(self):
        self.root = None

    def add(self, number):
        node = TreeNode(number)

        if self.root == None:
            self.root = node
            Tree.lis.append(self.root)
        else:
            while True:
                point = Tree.lis[0]

                if point.left == None:
                    point.left = node
                    Tree.lis.append(point.left)
                    return
                elif point.right == None:
                    point.right = node
                    Tree.lis.append(point.right)
                    Tree.lis.pop(0)
                    return

    def breadh_travel(self):
        """广度优先遍历"""
        if self.root is None:
            return
        queue = list()
        queue.append(self.root)
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.val, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def preorder_travel(self, root):
        """先序 根 左 右"""
        if root:
            print(root.val, end=" ")
            self.preorder_travel(root.left)
            self.preorder_travel(root.right)

    def inorder_travel(self, root):
        """中序 左 根 右"""
        if root:
            self.inorder_travel(root.left)
            print(root.val, end=" ")
            self.inorder_travel(root.right)

    def postorder_travel(self, root):
        """后序 左 右 根"""
        if root:
            self.postorder_travel(root.left)
            self.postorder_travel(root.right)
            print(root.val, end=" ")




if __name__ == '__main__':
    tree = Tree()
    p_tree = Tree()
    q_tree = Tree()
    L = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    for x in L:
        tree.add(x)
    p_tree.add(5)
    q_tree.add(4)
    way = Solution()
    result=way.lowestCommonAncestor(tree.root, p_tree.root, q_tree.root)
    print(result.val)

