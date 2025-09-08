class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # 插入节点
    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._insert(node.left, data)
        elif data > node.data:
            node.right = self._insert(node.right, data)
        return node

    # 查找节点
    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search(node.left, data)
        return self._search(node.right, data)

    # 删除节点
    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if node is None:
            return None
        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:  # 找到节点
            # 1. 只有一个子节点或无子节点
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # 2. 有两个子节点 -> 找右子树最小值替代
            min_larger_node = self._find_min(node.right)
            node.data = min_larger_node.data
            node.right = self._delete(node.right, min_larger_node.data)
        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    # 中序遍历（左 -> 根 -> 右）
    def inorder(self):
        res = []
        self._inorder(self.root, res)
        return res

    def _inorder(self, node, res):
        if node:
            self._inorder(node.left, res)
            res.append(node.data)
            self._inorder(node.right, res)

    # 前序遍历（根 -> 左 -> 右）
    def preorder(self):
        res = []
        self._preorder(self.root, res)
        return res

    def _preorder(self, node, res):
        if node:
            res.append(node.data)
            self._preorder(node.left, res)
            self._preorder(node.right, res)

    # 后序遍历（左 -> 右 -> 根）
    def postorder(self):
        res = []
        self._postorder(self.root, res)
        return res

    def _postorder(self, node, res):
        if node:
            self._postorder(node.left, res)
            self._postorder(node.right, res)
            res.append(node.data)


# 使用示例
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    print("中序遍历:", bst.inorder())     # [20, 30, 40, 50, 60, 70, 80]
    print("前序遍历:", bst.preorder())   # [50, 30, 20, 40, 70, 60, 80]
    print("后序遍历:", bst.postorder()) # [20, 40, 30, 60, 80, 70, 50]

    print("查找 40:", bst.search(40) is not None)  # True
    print("查找 100:", bst.search(100) is not None) # False

    bst.delete(70)  # 删除节点
    print("删除 70 后中序遍历:", bst.inorder()) # [20, 30, 40, 50, 60, 80]
