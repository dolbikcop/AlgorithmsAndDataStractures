from typing import List


class Node:
    def __init__(self, x, parent, height: int):
        self.height = height
        self.value = x
        self.parent = parent
        self.left = None
        self.right = None


class BinaryTree:
    root: Node

    def __init__(self, root: Node = None):
        self.root = root

    def from_array(self, arr: List[int], l, r: int, height=0):
        if l + 1 > r:
            return None
        elif l + 1 == r:
            return Node(arr[l], None, height)
        m = (l + r - 1) // 2
        t = Node(arr[m], None, height)
        t.left = self.from_array(arr, l, m, height + 1)
        t.right = self.from_array(arr, m + 1, r, height + 1)
        if t.left is not None:
            t.left.parent = t
        if t.right is not None:
            t.right.parent = t
        return t

    def show(self, current: Node, hasBro=False, ends = []):
        if current is not None:
            for i in range(len(ends)-1):
                print(f'{"│" if ends[i] else " "}', end='   ')
            print(f'{"├" if hasBro else "└"}', end='───')
            print(current.value)
            self.show(current.left, current.right is not None, ends + [True])
            self.show(current.right, False, ends + [False])


def main():
    arr = list(map(int, input().split()))
    tree = BinaryTree()
    tree.root = tree.from_array(arr, 0, len(arr))
    tree.show(tree.root)


main()
