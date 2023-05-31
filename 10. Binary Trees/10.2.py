from typing import List


class Node:
    def __init__(self, x, parent):
        self.value = x
        self.parent = parent
        self.left = None
        self.right = None


class BinaryTree:
    root: Node

    def __init__(self, root: Node = None):
        self.root = root

    def from_array(self, arr: List[int], l, r: int):
        if l + 1 > r:
            return None
        elif l + 1 == r:
            return Node(arr[l], None)
        m = (l + r - 1) // 2
        t = Node(arr[m], None)
        t.left = self.from_array(arr, l, m)
        t.right = self.from_array(arr, m + 1, r)
        if t.left is not None:
            t.left.parent = t
        if t.right is not None:
            t.right.parent = t
        return t

    def show(self, current: Node, ends: List[bool], hasBro: bool = False):
        if current is None:
            return
        predict = ''
        if len(ends) != 0:
            for i in range(len(ends) - 1):
                predict += "│   " if ends[i] else "    "

            predict += "├───" if hasBro else "└───"

        print(predict + str(current.value))
        self.show(current.left, ends + [current.right is not None], current.right is not None)
        self.show(current.right, ends + [False], False)

    def __find(self, v: Node, x: int) -> Node:
        if v is not None:
            if v.value == x:
                return v
            elif v.value > x:
                return self.__find(v.left, x)
            else:
                return self.__find(v.right, x)

    def find(self, x: int) -> Node:
        return self.__find(self.root, x)

    def __delete(self, t: Node) -> None:
        if t is None:
            return
        if (t.left is None) or (t.right is None):
            if t.left is not None:
                child = t.left
            else:
                child = t.right
            if t == self.root:
                self.root = child
                if child is not None:
                    child.parent = None
            if t.parent.left == t:
                t.parent.left = child
                if child is not None:
                    child.parent = t.parent
            else:
                t.parent.right = child
                if child is not None:
                    child.parent = t.parent
        else:
            nxt = t.right
            while nxt.left is not None:
                nxt = nxt.left
            t.value = nxt.value
            self.__delete(nxt)

    def delete(self, x: int) -> None:
        if self.root is not None:
            t = self.find(x)
            if t is not None:
                self.__delete(t)

    def __add(self, v: Node, x: int) -> None:
        if v is not None:
            if x < v.value:
                if v.left is None:
                    v.left = Node(x, v)
                    return
                self.__add(v.left, x)
            else:
                if v.right is None:
                    v.right = Node(x, v)
                    return
                self.__add(v.right, x)

    def add(self, x: List[str]) -> None:
        for i in x:
            self.__add_item(int(i))

    def __add_item(self, x: int):
        if self.root is None:
            self.root = Node(x, None)
            return
        self.__add(self.root, x)

    def next(self, val: int) -> Node:
        v = self.find(val)
        if v == None:
            return None
        if v.right != None:
            nxt = v.right
            while nxt.left != None:
                nxt = nxt.left
            return nxt.value
        nxt = v
        while (nxt.parent != None) and (nxt.parent.right == nxt):
            nxt = nxt.parent
        return nxt.parent.value if nxt.parent is not None else None

def main():
    arr = list(map(int, input().split()))
    tree = BinaryTree()
    tree.root = tree.from_array(arr, 0, len(arr))
    is_not_exit = True

    while is_not_exit:
        command = input().split()
        if len(command) == 1:
            is_not_exit = command[0] != 'exit'
            if command[0] == 'print':
                tree.show(tree.root, [])
        elif command[0] == 'delete':
            tree.delete(int(command[1]))
            print('Ok')
        elif command[0] == 'add':
            tree.add(command[1:])
            print('Ok')
        elif command[0] == 'find':
            v = tree.find(int(command[1]))
            print('Число нашлось' if v is not None else 'Число не нашлось')
        elif command[0] == 'next':
            v = tree.next(int(command[1]))
            print(v if v is not None else 'Следующего числа нет')

main()
