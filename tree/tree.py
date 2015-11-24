# -*- coding: utf-8 -*-

__author__ = 'xiaowang'
__date__ = '15-11-18'


class Node(object):
    """节点类"""

    def __init__(self, data=None, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


class Tree(object):
    def __init__(self):
        self.root = Node()

    """递归实现前序遍历"""

    def rec_pre_order(self, node=None):
        if node:
            print(node.data, end=" ")
            self.rec_pre_order(node.left_child)
            self.rec_pre_order(node.right_child)

    """非递归实现前序遍历"""

    def pre_order(self):
        ls = []
        if self.root:
            ls.append(self.root)
        while len(ls):
            node = ls.pop()
            print(node.data)
            if node.right_child:
                ls.append(node.right_child)
            if node.left_child:
                ls.append(node.left_child)

    """递归实现中序遍历"""

    def rec_in_order(self, node):
        if node:
            self.rec_in_order(node.left_child)
            print(node.data, end=" ")
            self.rec_in_order(node.right_child)

    def in_order(self):
        ls = []
        node = self.root
        while node or len(ls):
            while node:
                ls.append(node)
                node = node.left_child
            if len(ls):
                node = ls.pop()
                print(node.data, end=" ")
                node = node.right_child

    """后序遍历"""

    def rec_post_order(self, node):
        if node:
            self.rec_post_order(node.left_child)
            self.rec_post_order(node.right_child)
            print(node.data, end=" ")




    """计算树的深度"""

    def get_depth(self):
        """
        递归树的左右节点,取值大的深度
        :return:
        """

        def _depth(node):
            if not node:
                return 0
            else:
                left_depth = _depth(node.left_child)
                right_depth = _depth(node.right_child)
                return left_depth + 1 if left_depth > right_depth else right_depth + 1

        return _depth(self.root)

    def get_leaves(self):
        pass


if __name__ == '__main__':
    tree = Tree()
    tree.root = Node('A')
    tree.root.left_child = Node('B')
    tree.root.right_child = Node('C')
    tree.root.left_child.left_child = Node('D')
    tree.root.left_child.right_child = Node('E')
    tree.root.left_child.right_child.right_child = Node('F')
    tree.root.left_child.left_child.right_child = Node('G')

    # tree.rec_pre_order(tree.root)
    # print()

    # tree.rec_in_order(tree.root)
    # print()
    # tree.in_order()
    tree.rec_post_order(tree.root)
    print()
    tree.post_order()
    # print(root.data)
    # root.
    # print(tree.get_depth())
    # tree.pre_order()
