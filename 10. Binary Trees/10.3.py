from typing import List


class Node:
    def __init__(self, x: int, parent):
        self.x = x
        self.parent = parent
        self.l = None
        self.r = None


class Tree:
    def __init__(self):
        self.root = None

    def __add(self, v: Node, x: int) -> None:
        if v is not None:
            if x < v.x:
                if v.l is None:
                    v.l = Node(x, v)
                    return
                self.__add(v.l, x)
            else:
                if v.r is None:
                    v.r = Node(x, v)
                    return
                self.__add(v.r, x)

    def add(self, x: int) -> None:
        if self.root is None:
            self.root = Node(x, None)
            return
        self.__add(self.root, x)

    def from_array(self, arr: List[int]):
        self.root = self.__from_array(arr, 0, len(arr))

    def __from_array(self, arr: List[int], l, r: int):
        if l + 1 > r:
            return None
        elif l + 1 == r:
            return Node(arr[l], None)
        m = (l + r - 1) // 2
        t = Node(arr[m], None)
        t.l = self.__from_array(arr, l, m)
        t.r = self.__from_array(arr, m + 1, r)
        if t.l is not None:
            t.l.parent = t
        if t.r is not None:
            t.r.parent = t
        return t

    def __find(self, v: Node, x: int) -> Node:
        if v is not None:
            if v.x == x:
                return v
            elif v.x > x:
                return self.__find(v.l, x)
            else:
                return self.__find(v.r, x)

    def find(self, x: int) -> Node:
        return self.__find(self.root, x)

    def __delete(self, t: Node) -> None:
        if t is None:
            return
        if (t.l is None) or (t.r is None):
            if t.l is not None:
                child = t.l
            else:
                child = t.r
            if t == self.root:
                self.root = child
                if child is not None:
                    child.parent = None
            if t.parent.l == t:
                t.parent.l = child
                if child is not None:
                    child.parent = t.parent
            else:
                t.parent.r = child
                if child is not None:
                    child.parent = t.parent
        else:
            nxt = t.r
            while nxt.l is not None:
                nxt = nxt.l
            t.x = nxt.x
            self.__delete(nxt)

    def delete(self, x: int) -> None:
        if self.root is not None:
            t = self.find(x)
            if t is not None:
                self.__delete(t)

    def min(self, current: Node):
        if current is None:
            return None
        if current.l is not None:
            return self.min(current.l)
        else:
            return current
    def max(self, current: Node):
        if current is None:
            return None
        if current.r is not None:
            return self.max(current.r)
        else:
            return current
    def list(self, current: Node):
        if current is not None:
            self.list(current.l)
            print(current.x, end=' ')
            self.list(current.r)


def main():
    arr = list(map(int, input().split()))
    tree = Tree()
    tree.from_array(arr)
    while True:
        command = input().split()
        if command[0] == 'exit':
            break
        elif command[0] == 'delete':
            tree.delete(int(command[1]))
            print('Ok')
        elif command[0] == 'find':
            if tree.find(int(command[1])) is not None:
                print('Такая банка есть')
            else:
                print('Такой банки нет')
        elif command[0] == 'min':
            m = tree.min(tree.root)
            print(m.x if m is not None else 'Склад пуст')
        elif command[0] == 'max':
            m = tree.max(tree.root)
            print(m.x if m is not None else 'Склад пуст')
        elif command[0] == 'list':
            tree.list(tree.root)
            print()
        elif command[0] == 'add':
            print('Ok')
            tree.add(int(command[1]))


main()
